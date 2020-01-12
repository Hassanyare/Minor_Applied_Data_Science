# Git commit records

The table below are links to the contribution to the project group in the form of all the commits I submitted.

|Commit Hash (link)| Date | Branch | Description |
| ----------------:|-----:| ------:| -----------:|
[9a32087](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/9a320875851e844fa30dc27a3242c40b76b7c0d4)|2019-12-18T15:24:02+01:00||- cnn2 cleaned - cnn2 the conv2d size = 1, width
[f3fbf84](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/f3fbf84436bdac4def015ffc25107cd38c177d0f)|2019-12-17T17:08:26+01:00||-  exercise.py contains lowpass filter and differentiation. - exercises have now the maximum length of frames(577).This is realised with zero padding.
[66b0d06](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/66b0d0603f02bc375286f3bd7e24c4436ba5d32e)|2019-12-17T14:47:33+01:00||data-clean fetched from master2.0
[6a8cd2c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/6a8cd2c5e676737316c5004011d94663f7f32012)|2019-12-17T14:46:00+01:00||beginning with data preparation
[4134d16](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/4134d161421787f6cc3e280d8119c99af7450148)|2019-12-15T12:38:33+01:00|origin/dev_hassan|- added function to filter left and righ arm into exercises - wrote code to clf left and right arm movement with LOGRegression
[c1338b4](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c1338b44b638ea06c3b8c4e34164a7ac44d19cba)|2019-12-12T17:15:09+01:00||spelling changes
[c535040](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c535040eb9d22d163de734f76e968961047b5422)|2019-12-12T17:08:26+01:00||-cleaned branch dev_hassan -main now contains only the code to load the data and execute the logistic regression model. - exercise is now cleaned - the rest of the code is has minor changes
[7cca92b](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/7cca92b1c917290050280c3eb644e179f4889bce)|2019-12-12T12:41:56+01:00||-  working LSTM model on data with shape (samples, 100, 120) - dataLSTM now contains function to create data with the shape (sample, 100, 24) -config now contains hyper_LSTM
[6a96f0d](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/6a96f0dd3d59bf19a582a80d7f97e6a13588783e)|2019-12-11T22:34:40+01:00||RUN model a twice on different configurations *see modeloutput.json
[deeb447](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/deeb4474c107d07c81589662ec9d1d1fbab89494)|2019-12-11T22:04:20+01:00||- created cnn_logger function - logged the shape, hyper_parameters, model summary and model history into file modeloutput.json
[b4bcf05](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/b4bcf05ac269066748a8df326b6560ec3b90adb5)|2019-12-10T16:11:30+01:00||- splitted hyper_cnn class in config into 2 cls - created a dictionary out of class hyper_cnn - created a dictionary out of the shape input data - saved model.summary into file modelsummary.txt - saved both the shape dict, and hyper cnn dict into the modelsummary.txt file
[05d94bb](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/05d94bbca50239524a60b44eb6552907956cc42d)|2019-12-09T23:05:39+01:00||- splitted data into train test data - working model on the newly generated data
[c703361](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c7033618bd0d9a7e8dd25ca33ed2d0b7bb0a1ab1)|2019-12-09T19:07:14+01:00||-prepared data in shape (frames, bones, axis) see dataCNN2 - samples are exercises instead of exercise combinations - created CNN2 a new cnn for the new data format - added parameter bone_count indicating the total bones
[e8e6605](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/e8e66056900f84e95baf6b669ec0a34ba99949cc)|2019-12-09T16:32:11+01:00||-re named the hyper_parameters to more understanding names - added strides into config
[d5ca175](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/d5ca1752ea120ebacb63c02c8c91f898bfed8b7d)|2019-12-07T10:52:12+01:00||- a working lstm model, - changed name nn to lstm - changed name data2 to dataLSTM
[8c57247](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8c57247282efa03b9d2bf521737d8b85af155eea)|2019-12-06T16:25:10+01:00||added config.framecount improved architecture
[45f624a](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/45f624a69ab812cb9f34460e15ed4b728163a06e)|2019-12-06T14:42:40+01:00||added -tensorboard
[7159ff2](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/7159ff2a8816d09cc880c9b69ebb69a92903b63d)|2019-12-05T16:11:26+01:00||added to CNN2() -hyperconfig -early stopping -ToDo
[46b3d17](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/46b3d17eefd7a820c118eb41a821989eca03057f)|2019-12-05T15:34:32+01:00||working CNN model with standard optimizations
[73ac025](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/73ac0251807dc4a89c344a8c4ccd8b876fea9e09)|2019-12-04T11:43:11+01:00||test environment
[ac1c60c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/ac1c60c3a2cf626e1b0fe120d814799f72dd60f2)|2019-12-04T10:52:51+01:00||renamed file lstm to nn
[3795f7c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/3795f7c640d213e23e19dbc27adef5eb654f910e)|2019-12-03T22:32:48+01:00||Convolutional Neural Networks on resampled data
[6a08733](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/6a087338d3981612ca6ad8ed53efa0fd27beae29)|2019-12-03T20:44:35+01:00||enco-dec_opzet
[1aafd35](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/1aafd35ec5f84a940e661cefefa4ec8b1d2fd673)|2019-12-03T13:05:44+01:00||model lstm as fun
[c70d504](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c70d5040c8da1e0226725d8a49eaaecd49f68abc)|2019-12-03T13:00:17+01:00||lstm model with data shape(x,100,130)
[f3d59ee](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/f3d59eefbe2e9b48dfb4a21cb80b04075f6fbdd9)|2019-12-03T12:18:22+01:00||LSTM model with resampled data (x,130,100)
[2713727](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/27137274de918a86c08fbe5af90ed746eb5a95f1)|2019-11-30T14:15:08+01:00||concept LSTM model changed data shape 672,100,130.
[3c5a23b](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/3c5a23ba2e48e1d06b9a9cecde8c4c9ceddbe86f)|2019-11-21T12:35:29+01:00||remove idle cleaned version
[10b7cc3](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/10b7cc396c5845503054c9eb20b69db08fe44b14)|2019-11-21T12:32:46+01:00||remove idle now works on split 5, with exceptions
[591fc85](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/591fc85c1e13bc4489f27320eec5f2d090bb77a5)|2019-11-19T14:37:03+01:00||copied ml files to do LGR on Left vs righ
[c0717c5](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c0717c5682312730f1c9ddf509be3c4ac8a9fccd)|2019-11-19T14:24:19+01:00||NEW_left_vs_Right clf
[a2e9f3b](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/a2e9f3bb5e669e5e23dbeaaa0384130ed3b6a7c6)|2019-11-14T21:01:31+01:00||idle :- diff calculations for diff exe
[7783fd4](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/7783fd47178703525af7c233b4b2dc16bc2b9698)|2019-11-14T20:39:21+01:00||Merge branch 'master2.0' of ssh.dev.azure.com:v3/DataScienceMinor/Data%20Science/Data%20Science into master2.0
[787f1b7](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/787f1b727258b71e1e06e0395800dd94fc6f6ea5)|2019-11-14T20:28:06+01:00||visualis.py contains func to visualise idle,
[386f970](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/386f9700b1b7f628f2b56bb83c9eb4a79dd1df85)|2019-11-14T13:16:18+01:00||Merge branch 'master2.0' of ssh.dev.azure.com:v3/DataScienceMinor/Data%20Science/Data%20Science into master2.0
[a163c61](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/a163c61c7638565ad13f04300f16eda46face4d6)|2019-11-14T13:09:25+01:00||remove_idle works and  run model LRG on new df
[4203299](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/42032997f99e0f20b2ea776982eed1cc72993856)|2019-11-12T19:52:31+01:00||implimented  remove_idle version 1 on all the data
[83171ed](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/83171ed59994a5f30032342e7accaa9d2a21fed3)|2019-11-12T13:56:22+01:00||Merge branch 'master2.0' of ssh.dev.azure.com:v3/DataScienceMinor/Data%20Science/Data%20Science into master2.0
[05db150](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/05db15081a5b7e5f6d45092532c3dae4c1035ff0)|2019-11-12T13:56:17+01:00||generated new dataframe after removing idle
[2b5adaf](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/2b5adaf974b3461a5f389117a0645d555331036b)|2019-11-12T13:27:49+01:00||returns the correct value of endindex
[dec4a7c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/dec4a7c0e7d5750a277a2907170c8e412a2780ce)|2019-11-11T18:48:52+01:00||space_description by Tony
[89ef67f](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/89ef67f0c1c5f93f443995232bc284d1fecebd4f)|2019-11-11T12:59:14+01:00||generated new 'clean' dataframe using get_index
[92c6e94](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/92c6e94ae10c048be9cafed597eeea3c87036ae1)|2019-11-10T15:41:06+01:00||trying to put the function to get the idle in cl
[1a390cb](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/1a390cbab20f2e1b84eb79bbaf08e53f5b2a2fcb)|2019-11-08T16:19:14+01:00||generate new dataframe concept
[6207f31](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/6207f3115f4f06b4a95fab5890a242e06d68658e)|2019-11-08T16:11:06+01:00||i have de fun(get_idle) into  Class exercises
[06efae1](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/06efae15fd26da68230dd77bdc513269032ba66e)|2019-11-07T20:08:38+01:00||try to execute code on patient level
[645595a](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/645595ace124155a54170534804b13ac3e96934e)|2019-11-06T17:46:01+01:00||concept_detecting idle in exercises
[8092a02](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8092a02cae788debe1c5462d8caf051affc7e6ec)|2019-11-05T18:42:41+01:00||Visualization
[1f1c040](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/1f1c0408df35b7b6851de7707ed45a3d06181e00)|2019-11-01T13:10:42+01:00||test_selection in config & exceptions
[dae6bb7](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/dae6bb79d7f83484286736c178bfe0d130b523b6)|2019-10-31T15:19:22+01:00||able to split test/train data
[0f153f7](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/0f153f723686b39ffdcab0dac312d614f26466ec)|2019-10-31T11:03:43+01:00||last modification rebuilding 650clms
[e4cd334](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/e4cd33469f64a460c387f2692de18c701f17ab9f)|2019-10-29T10:34:13+01:00||tsne_data opzet
[627a4b3](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/627a4b33caf7c95c8ee5b66f07e8bd3f1b5780d1)|2019-10-25T12:07:37+02:00||file for later use, tring tsne + bigger plt _ main
[ae0bd8a](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/ae0bd8ad1f80ff07d4d61bebc8e6a91169f892a3)|2019-10-25T00:02:33+02:00||t-sne model concept succesfully implimented
[96b038d](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/96b038df31778bf312497215a4c9aef04e6f9af8)|2019-10-22T15:43:25+02:00||changed the path of  LRG model
[5917a76](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/5917a7637684b9442d82ed8e23ac050265153798)|2019-10-22T15:08:09+02:00||re-arranged_files & created_decisionTree_model
[0b70abc](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/0b70abc1a7a031c15499e35a79dcd94849dfc746)|2019-10-22T10:10:36+02:00||rearached files into folders
[304476e](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/304476ee8d14e61ff04782ada34f8df77daa68b5)|2019-10-18T17:16:36+02:00||Generated 650 columns and implimeted  ML-LRG
[7091db4](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/7091db45bd3ae6f023018d7d95d4667388fc68ce)|2019-10-18T08:32:28+02:00||removes mistakes in the code
[c7eab47](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c7eab472f643ef840b0017b3f87f0d8bbac8e89b)|2019-10-17T18:53:38+02:00||crossjoined exercises and made 5 frames of each ex
[0f986e1](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/0f986e15aefe7153014975595d5fcf2b2a7d9d1b)|2019-10-17T15:50:54+02:00||all categories are loaded
[efa7b30](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/efa7b3071e061103e340ba58b53eda3bb79308ff)|2019-10-17T15:43:26+02:00||imported all data from each category
[126c4d6](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/126c4d624f69f0b9398cb86cb20c1d0ecefd2fa9)|2019-10-16T17:05:55+02:00||onnodige codes uitgehaald
[8902d52](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8902d520bccf1584d74e18c2a49c2a6547fffc29)|2019-10-16T15:42:54+02:00||looping through list dir
[7eaa071](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/7eaa071b82f0ea83fc9d3776614c6c03189723a8)|2019-10-16T15:39:06+02:00||created list patient group
[b5236df](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/b5236df1bcd2ef3c30d0be511b870818248a18bd)|2019-10-16T15:08:34+02:00||opzet data processing
[9441c99](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/9441c99f0585b7f59b63e24905bcdc13eae6073e)|2019-10-16T11:14:23+02:00||changed file name src to leftVSright
[8d47ddc](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8d47ddc2a2cad5043e28ff1e572498d7c3926dda)|2019-10-15T15:56:14+02:00||test
[769e92e](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/769e92ee58c51bc552e056c1080ce1d3f7f2e70f)|2019-10-03T16:46:55+02:00|origin/MachineLearning|Datahandler for  accesing data and manipulating
[2fdae8e](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/2fdae8ec283e3c14b3b9ab58a202eac31c1d0e6a)|2019-10-02T21:36:42+02:00||new_parser for reading all data
[f093399](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/f0933996c781ef9fa4b1e5fa6377692ed0934235)|2019-10-01T11:34:52+02:00||depth = 4
[87c750a](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/87c750a3f09885d1b43670a763066af214189dea)|2019-09-30T20:45:46+02:00||made Decision Tree clf on left and right arm
[3ffd318](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/3ffd318119c9b87a759844726f40be3585dc0502)|2019-09-30T17:06:03+02:00||model KNeighbors is done
[8724f20](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8724f2036654632cef1be79d9b445c86d4f828b0)|2019-09-30T16:09:08+02:00||new model, knn
[d5fbf3f](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/d5fbf3f610ab505081ff3c577bef3bd564375c15)|2019-09-30T15:59:51+02:00||made a new model, Kneigbors. changed src.
[945f6c8](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/945f6c85e800e022624377a14858d157a3246c89)|2019-09-30T09:30:47+02:00||modified main
[1df7255](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/1df72558a6b04d118ee8fb81068e3268d2bf3b1c)|2019-09-30T09:30:29+02:00||built knn model
[05350a7](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/05350a7ac187e1fece0ff03b10e541ee2c45a140)|2019-09-27T13:40:38+02:00||Ml_knn_model
[3b2fe22](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/3b2fe22b1a68da6762f4bfed6b1cf31a0fed8006)|2019-09-27T13:38:51+02:00||created KNN_model
[b755673](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/b755673d33af3e2f862af008dee886d125cb09d6)|2019-09-27T09:38:09+02:00||model_using_svc
[81bc27c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/81bc27cea27636978a7b4eeb4e4740b07ef3be5f)|2019-09-27T09:00:12+02:00||re_mapping master: dev_hassan
[c4a07ca](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/c4a07caec77ea1ddbd94e91f747dddd055dfacd7)|2019-09-26T10:58:10+02:00||getting started with ML: changed path and etc
[0a7cff8](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/0a7cff8495726edc814fdec2a544735c2d86e009)|2019-09-25T17:21:07+02:00||2D_vzs+ coping all the other maps
[da0359e](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/da0359e5ebf7586de303749cc7ac06f1a12cb0e2)|2019-09-25T10:32:24+02:00||new_visualization
[72303cd](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/72303cd6b130f035794f10480ab36167586e735f)|2019-09-25T10:29:04+02:00||copy of parser
[e63d37a](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/e63d37a5c8e57dc647533e3c4cb39f37b15f0b0a)|2019-09-25T07:19:36+02:00||copy of the data
[4536b64](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/4536b64f73f3086c63d3bc028ade083ac8c74156)|2019-09-25T07:18:48+02:00||made copy of the data
[0fe66c2](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/0fe66c2777e15c06eca613c2291ce93858b0e401)|2019-09-24T15:30:02+02:00||Merge branch 'MachineLearning' of ssh.dev.azure.com:v3/DataScienceMinor/Data%20Science/Data%20Science into MachineLearning
[507155c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/507155cdf2155c12d43fedfc4e1b398cd36dfed7)|2019-09-24T15:29:52+02:00||added #%%
[6fc0b49](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/6fc0b4947672bf5df5a77cf774193cf0bc387a98)|2019-09-24T15:29:25+02:00||making Class  src DataCamp
[f7bca18](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/f7bca18881f74f1f1021ccd8622d077dac087ace)|2019-09-23T16:01:53+02:00||Deleted file 2D visualization Hassan
[109fc9f](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/109fc9f30ac41ee5538caf7407747c0099a8eec0)|2019-09-23T15:59:14+02:00||visualization map
[bd476ad](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/bd476ad091a9b8e2c9965699b872f562d3e0222c)|2019-09-23T12:28:23+02:00||coby_body
[3783c68](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/3783c6815db15367bb53dabfb942962859f7ae24)|2019-09-21T23:08:11+02:00||Axis
[4054345](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/4054345fd85ff814becb3fb50f677f66b1988b04)|2019-09-21T01:14:37+02:00||change path csv file
[cd381eb](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/cd381eba819ae0071b03642ff53b4103995b6bf1)|2019-09-21T00:59:06+02:00||Setting-up interface
[8ea1ed9](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8ea1ed95687c2bf382eb60288e289af984379ed1)|2019-09-20T16:02:17+02:00||space
[a5bd29c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/a5bd29cf56b8a4b650d0265ab8b8ca77f6dae718)|2019-09-20T11:57:05+02:00||space-verwijderd
[8a57240](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8a5724077f573920c8ebccd8da0b3f4715502e6c)|2019-09-10T16:22:53+02:00||Visualization-2D.by_hassan
[5ed8e5c](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/5ed8e5ca235f6ca2f0feea0fb08b09a561a86e9b)|2019-09-09T15:40:20+02:00||test-99
[8917fe0](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/8917fe059453d450b3d5a8712b3b5cbdfed817b1)|2019-09-09T15:35:38+02:00||Test doc verwijderd
[3d44bc1](https://dev.azure.com/DataScienceMinor/Data%20Science/_git/Data%20Science/commit/3d44bc1f2101a0836a91832a1fd8f03eb36a3afc)|2019-09-09T15:29:59+02:00||Test push




