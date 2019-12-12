import pprint



class config:
    basepath = "C:\\Users\\hassa\\OneDrive\\Desktop\\DataScience\\CODE\\data2.0\\Catagory_{groupid}"
    pp = pprint.PrettyPrinter(indent=4)
    columns = ["thorax_r_x", "thorax_r_y", "thorax_r_z",
               "clavicula_r_x", "clavicula_r_y", "clavicula_r_z",
               "scapula_r_x", "scapula_r_y", "scapula_r_z",
               "humerus_r_x", "humerus_r_y", "humerus_r_z",
               "ellebooghoek_r",
               "thorax_l_x", "thorax_l_y", "thorax_l_z",
               "clavicula_l_x", "clavicula_l_y", "clavicula_l_z",
               "scapula_l_x", "scapula_l_y", "scapula_l_z",
               "humerus_l_x", "humerus_l_y", "humerus_l_z",
               "ellebooghoek_l"]
    columns_2 = ["humerus_r_x", "humerus_r_y", "humerus_r_z"]

    test_selections = { '1': [1,5,18,20,27],
                        '2': [2, 3, 5, 19, 23, 29],
                        '3': [18,20,27, 30, 35, 38, 39],
                        '4': [1,5,18,20,27,10,32]
} 
    frames_counts = 5
    split = 3
    first_side = 0
    second_side = -1

