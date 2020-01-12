import numpy as np
from patient.patientgroup import PatientGroup
from tools.resample import resample_excercise
from config import config


colour_mapping = {
    'thorax_r': 45,
    'clavicula_r': 90,
    'scapula_r': 135,
    'humerus_r': 180,
    'thorax_l': 225,
    'clavicula_l': 275,
    'scapula_l': 315,
    'humerus_l': 360.
}


def create_colour_mapping(depth, length):
    generated_mapping = dict()
    for bone, colour in colour_mapping.items():
        generated_mapping[bone] = np.array([[colour] * depth] * length)

    return generated_mapping


def longest_exercise(patient_groups) -> int:
    """
    Retrieve the length of the exercise with the most data
    This is used to determine a fixed exercise length

    :param list patient_groups: patient groups to loop through
    :return: length of the longest exercise
    :rtype: int
    """

    longest_frame = -1
    # Get the longest exercise
    for patientgroup in patient_groups:
        for patient in patientgroup:
            for exercise in patient: 
                if len(exercise.dataframe) > longest_frame:
                    longest_frame = len(exercise.dataframe)
    
    return longest_frame


def exercise_padded(patient_groups) -> [PatientGroup]:
    """
    Create a fixed length exercise
    Exercises shorter than the determined length
    will be padded with zeros

    :param list patient_groups: list of patient groups to loop through
    :return: patient group with padded exercises embedded
    :rtype: list
    """
    longest_frame = longest_exercise(patient_groups)

    for patientgroup in patient_groups:
        for patient in patientgroup: 
            for exercise in patient:  
                np_exercise = exercise.np_data 
                np_velocity = exercise.differentiation

                len_exercises = exercise.lengte_exercise
                delta = (longest_frame - len_exercises)

                exercise.padded = np.pad(np_exercise, [(0, delta), (0, 0)], 'constant', constant_values=(0))
                exercise.v_padded = np.pad(np_velocity, [(0, delta), (0, 0)], 'constant', constant_values=(0))
                _mapping = create_colour_mapping(6, len_exercises)  # max depth, length
                for key in _mapping.keys():
                    _mapping[key] = np.pad(_mapping[key], [(0, delta), (0, 0)], 'constant', constant_values=(0))
                exercise.colour_map = _mapping

    return patient_groups


def generate_data_velocity(patient_groups):
    """
    Generate data for neural network learning

    :param list patient_groups: Patient groups to loop through
    :return: train and indicator data
    :rtype: list
    """
    longest_frame = longest_exercise(patient_groups)
    patient_groups = exercise_padded(patient_groups)

    np_output_exercises = np.zeros((0, longest_frame, config.bones_count, 6))
    np_output_indicator = np.array([])

    for patientgroup in patient_groups:
        for patient in patientgroup:
            for exercise in patient:
                np_exercise_comb = np.zeros((longest_frame, 0, 6))
                # pick the number of bones
                for index in range(config.bones_count):
                    # take the bone value from the padded exercise
                    np_exercise_bone = exercise.padded[:, 0 + index * 3:3 + index * 3]
                    np_exercise_bone_v = exercise.v_padded[:, 0 + index * 3:3 + index * 3]

                    # reshape the values into the desired format
                    np_exercise_bone = np.reshape(np_exercise_bone, (longest_frame, 1, 3))
                    np_exercise_bone_v = np.reshape(np_exercise_bone_v, (longest_frame, 1, 3))

                    # create a combination of the bone and velocity values
                    np_exe_bone_comb = np.dstack((np_exercise_bone, np_exercise_bone_v))
                    # add the combination to the complete exercise combination array
                    np_exercise_comb = np.append(np_exercise_comb, np_exe_bone_comb, axis=1)

                np_exercise_reshaped = np.reshape(np_exercise_comb, (1, longest_frame, config.bones_count, 6))
                np_output_exercises = np.concatenate((np_output_exercises, np_exercise_reshaped), axis=0)
                np_output_indicator = np.append(np_output_indicator, int(exercise.patientgroup) - 1)

        print('np_output_exercises, np_output_indicator: ', np_output_exercises.shape, np_output_indicator.shape)

    np_output_exercises = np_output_exercises % 360
    np_output_exercises = np_output_exercises / 360
    
    return [np_output_exercises, np_output_indicator]


def generate_data_velocity_colour(patient_groups):
    """
    Generate data for neural network learning

    :param list patient_groups: Patient groups to loop through
    :return: train and indicator data
    :rtype: list
    """
    depth = 6
    longest_frame = longest_exercise(patient_groups)
    patient_groups = exercise_padded(patient_groups)

    np_output_exercises = np.zeros((0, longest_frame, config.bones_count * 2, depth))
    np_output_indicator = np.array([])

    for patientgroup in patient_groups:
        for patient in patientgroup: 
            for exercise in patient:
                np_exercise_comb = np.zeros((longest_frame, 0, depth))
                # pick the number of bones
                for index in range(config.bones_count):
                    bone = '_'.join(config.columns[0 + index * 3].split('_')[:2])

                    # take the bone value from the padded exercise
                    np_exercise_bone = exercise.padded[:, 0+index*3:3+index*3]
                    np_exercise_bone_v = exercise.v_padded[:, 0+index*3:3+index*3]
                    np_exercise_bone_c = exercise.colour_map[bone][:,:depth]

                    # reshape the values into the desired format
                    np_exercise_bone = np.reshape(np_exercise_bone, (longest_frame, 1, 3))
                    np_exercise_bone_v = np.reshape(np_exercise_bone_v, (longest_frame, 1, 3))
                    np_exercise_bone_c = np.reshape(np_exercise_bone_c, (longest_frame, 1, depth))

                    # create a combination of the bone and velocity values
                    np_exe_bone_comb = np.dstack((np_exercise_bone, np_exercise_bone_v))
                    np_exe_bone_comb = np.hstack((np_exe_bone_comb, np_exercise_bone_c))
                    # add the combination to the complete exercise combination array
                    np_exercise_comb = np.append(np_exercise_comb, np_exe_bone_comb, axis=1)

                np_exercise_reshaped = np.reshape(np_exercise_comb, (1, longest_frame, config.bones_count * 2, 6))
                np_output_exercises = np.concatenate((np_output_exercises, np_exercise_reshaped), axis=0)
                np_output_indicator = np.append(np_output_indicator, int(int(exercise.patientgroup) - 1))

        print('np_output_exercises, np_output_indicator: ', np_output_exercises.shape, np_output_indicator.shape)

    np_output_exercises = np_output_exercises % 360
    np_output_exercises = np_output_exercises / 360

    return [np_output_exercises, np_output_indicator]


def generate_data_colour(patient_groups):
    """
    Generate data without velocity values

    :param list patient_groups: Patient groups to loop through
    :return: train and indicator data
    :rtype: list
    """
    longest_frame = longest_exercise(patient_groups)
    patient_groups = exercise_padded(patient_groups)

    np_output_exercises = np.zeros((0, longest_frame, config.bones_count * 2, 3))
    np_output_indicator = np.array([])

    for patientgroup in patient_groups:
        for patient in patientgroup:
            for exercise in patient:
                np_exercise = np.zeros((longest_frame, 0, 3))

                for index in range(8):
                    bone = '_'.join(config.columns[0 + index * 3].split('_')[:2])

                    np_exercise_bone = exercise.padded[:, 0+index*3:3+index*3]
                    np_exercise_bone_c = exercise.colour_map[bone][:,:3]

                    np_exercise_bone = np.reshape(np_exercise_bone, (longest_frame, 1, 3))
                    np_exercise_bone_c = np.reshape(np_exercise_bone_c, (longest_frame, 1, 3))

                    np_exe_bone_comb = np.hstack((np_exercise_bone, np_exercise_bone_c))
                    np_exercise = np.append(np_exercise, np_exe_bone_comb, axis=1)

                np_exercise_reshaped = np.reshape(np_exercise, (1, longest_frame, config.bones_count * 2, 3))
                np_output_exercises = np.concatenate((np_output_exercises, np_exercise_reshaped), axis=0)
                np_output_indicator = np.append(np_output_indicator, int(exercise.patientgroup) - 1)

    np_output_exercises = np_output_exercises % 360
    np_output_exercises = np_output_exercises / 360

    return [np_output_exercises, np_output_indicator]


def generate_data_padded(patient_groups):
    """
    Generate data without velocity values

    :param list patient_groups: Patient groups to loop through
    :return: train and indicator data
    :rtype: list
    """
    longest_frame = longest_exercise(patient_groups)
    patient_groups = exercise_padded(patient_groups)

    np_output_exercises = np.zeros((0, longest_frame, config.bones_count, 3))
    np_output_indicator = np.array([])

    for patientgroup in patient_groups:
        for patient in patientgroup:
            for exercise in patient:
                np_exercise = np.zeros((longest_frame, 0, 3))

                for index in range(8):
                    np_exercise_bone = exercise.padded[:, 0+index*3:3+index*3]

                    np_exercise_bone = np.reshape(np_exercise_bone, (longest_frame, 1, 3))

                    np_exercise = np.append(np_exercise, np_exercise_bone, axis=1)
                
                np_exercise_reshaped = np.reshape(np_exercise, (1, longest_frame, config.bones_count, 3))
                np_output_exercises = np.concatenate((np_output_exercises, np_exercise_reshaped), axis=0)
                np_output_indicator = np.append(np_output_indicator, int(exercise.patientgroup) - 1)
    
    np_output_exercises = np_output_exercises % 360
    np_output_exercises = np_output_exercises / 360

    return [np_output_exercises, np_output_indicator]


def resample_patient_groups(patient_groups):
    for patient_group in patient_groups:
        for patient in patient_group.patients:
            for exercise in patient.exercises:
                exercise.dataframe = resample_excercise(exercise.dataframe, config.frames_counts)
                exercise.np_data = exercise.dataframe.to_numpy()
                exercise.colour_map = create_colour_mapping(6, config.frames_counts)  # max depth, length

    return patient_groups


def generate_data_resampled(patient_groups):
    patient_groups = resample_patient_groups(patient_groups)

    np_output_exercises = np.zeros((0, config.frames_counts, config.bones_count , 3))
    np_output_indicator = np.array([])

    np.set_printoptions(threshold=np.inf)
    for patientgroup in patient_groups:
        for patient in patientgroup: 
            for exercise in patient: 
                np_exercise = np.zeros((config.frames_counts, 0, 3))

                for index in range(8): 
                    np_exercise_bone = exercise.np_data[:,0+index*3:3+index*3]
                    np_exercise_bone = np.reshape(np_exercise_bone, (config.frames_counts, 1, 3)) 
                    np_exercise = np.append(np_exercise, np_exercise_bone, axis=1)
                
                np_exercise_reshaped = np.reshape(np_exercise, (1, config.frames_counts, config.bones_count , 3))
                np_output_exercises = np.concatenate((np_output_exercises, np_exercise_reshaped), axis=0)
                np_output_indicator = np.append(np_output_indicator, int(int(exercise.patientgroup) - 1))

    np_output_exercises = np_output_exercises % 360
    np_output_exercises = np_output_exercises / 360

    return [np_output_exercises, np_output_indicator]


def generate_data_resampled_colour(patient_groups):
    patient_groups = resample_patient_groups(patient_groups)

    np_output_exercises = np.zeros((0, config.frames_counts, config.bones_count * 2, 3))
    np_output_indicator = np.array([])

    for patientgroup in patient_groups:
        for patient in patientgroup:
            for exercise in patient:
                np_exercise = np.zeros((config.frames_counts, 0, 3))

                for index in range(8):
                    bone = '_'.join(config.columns[0 + index * 3].split('_')[:2])

                    np_exercise_bone = exercise.np_data[:, 0 + index * 3:3 + index * 3]
                    np_exercise_bone_c = exercise.colour_map[bone][:,:3]

                    np_exercise_bone = np.reshape(np_exercise_bone, (config.frames_counts, 1, 3))
                    np_exercise_bone_c = np.reshape(np_exercise_bone_c, (config.frames_counts, 1, 3))

                    np_exe_bone_comb = np.hstack((np_exercise_bone, np_exercise_bone_c))
                    np_exercise = np.append(np_exercise, np_exe_bone_comb, axis=1)

                np_exercise_reshaped = np.reshape(np_exercise, (1, config.frames_counts, config.bones_count * 2, 3))
                np_output_exercises = np.concatenate((np_output_exercises, np_exercise_reshaped), axis=0)
                np_output_indicator = np.append(np_output_indicator, int(exercise.patientgroup) - 1)

    np_output_exercises = np_output_exercises % 360
    np_output_exercises = np_output_exercises / 360

    return [np_output_exercises, np_output_indicator]
