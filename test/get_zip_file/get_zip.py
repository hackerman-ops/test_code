# # -*- coding:utf-8 -*-
import zipfile
import os,sys
from os import path,system
import datetime
cur_dir3 = path.dirname(path.dirname(path.abspath(__file__)))
des_file = "/Users/lx/Desktop/bills_bills/"
print(cur_dir3)
a = [100000202555,100000202992,100000034610,100000034919,100000026945,100000203044,100000203164,100000202613,100000203251,100000202722,100000203377,100000024343,100000027371,100000025875,100000026276,100000026341,100000024414,100000004385,100000026763,100000167143,100000026851,100000027064,100000027273,100000025111,100000144834,100000202896,100000203434,100000203519,100000203644,100000203757,100000028199,100000029027,100000029180,100000008264,100000029361,100000029422,100000029631,100000029710,100000102060,100000098628,100000149794,100000203847,100000208411,100000004193,100000006115,100000006237,100000140777,100000023192,100000156476,100000138528,100000106440,100000207288,100000207356,100000207450,100000207561,100000204227,100000204138,100000024566,100000024698,100000168397,100000024796,100000024928,100000040384,100000144743,100000133922,100000204394,100000204498,100000204572,100000204685,100000158919,100000026633,100000008392,100000026576,100000105547,100000028521,100000028340,100000019944,100000204732,100000204890,100000204942,100000028619,100000205034,100000205178,100000205274,100000205366,100000205482,100000028776,100000028239,100000028480,100000168531,100000166432,100000030519,100000030612,100000030726,100000030889,100000030986,100000008691,100000182340,100000008775,100000031037,100000008595,100000030092,100000030143,100000030221,100000030346,100000030477,100000031243,100000008932,100000009016,100000009136,100000009240,100000009362,100000009483,100000206136,100000208575,100000208623,100000009515,100000206243,100000031325,100000031581,100000031750,100000031628,100000008878,100000006413,100000139996,100000031191,100000206399,100000135655,100000140497,100000100833,100000138235,100000145488,100000009870,100000009917,100000206455,100000206516,100000206661,100000206748,100000207677,100000207742,100000207862,100000207969,100000016895,100000015045,100000016664,100000016764,100000107617,100000016316,100000016188,100000016274,100000016943,100000017072,100000017234,100000099047,100000107347,100000031446,100000014529,100000102686,100000107144,100000040441,100000206850,100000144970,100000206959,100000207054,100000207195,100000019584,100000019654,100000019716,100000019855,100000025294,100000182420,100000019434,100000014669,100000035233,100000208047,100000107982,100000166392,100000023255,100000106991,100000208122,100000208254,100000208363,100000208850,100000031858,100000031914,100000032077,100000032270,100000023046,100000151778,100000021213,100000156038,100000208760,100000103928,100000032166,100000057839,100000033058,100000033127,100000022359,100000143073,100000050648,100000051390,100000050853,100000133797,100000057772,100000057980,100000058066,100000058163,100000058271,100000058328,100000059750,100000057452,100000022210,100000032380,100000032480,100000032648,100000169781,100000059953,100000060057,100000208974,100000032855,100000032976,100000032528,100000143957,100000060336,100000209025,100000209154,100000060535,100000060754,100000061473,100000151357,100000067244,100000067525,100000151191,100000141490,100000193615,100000138129,100000145527,100000150824,100000101447,100000209221,100000193520,100000169833,100000161030,100000193773,100000171386,100000170185,100000152056,100000098023,100000144112,100000171479,100000170468,100000160895,100000170364,100000165922,100000152285,100000160758,100000160155,100000169947,100000160359,100000171123,100000171284,100000209312,100000161170,100000162880,100000170056,100000035155,100000170549,100000139252,100000011053,100000010811,100000160599,100000171778,100000171663,100000010939,100000170243,100000098146,100000013899,100000013913,100000172063,100000171817,100000013659,100000098991,100000151863,100000099527,100000014027,100000014165,100000014492,100000014285,100000014341,100000014761,100000165668,100000159861,100000160492,100000159962,100000152150,100000013784,100000018247,100000018337,100000197067,100000196858,100000194968,100000194523,100000171990,100000194358,100000194869,100000197498,100000197392,100000197141,100000108611,100000140546,100000108832,100000018019,100000194657,100000104727,100000020361,100000020442,100000196343,100000197594,100000197661,100000104949,100000105129,100000155582,100000104556,100000197256,100000209525,100000209635,100000196537,100000033367,100000033443,100000067713,100000034764,100000151592,100000024148,100000060220,100000080631,100000104238,100000072987,100000168265,100000033250,100000069445,100000080145,100000080981,100000080748,100000081414,100000002224,100000068798,100000034063,100000034131,100000034283,100000081185,100000004749,100000143832,100000081542,100000082428,100000083265,100000082189,100000082381,100000082580,100000082630,100000082888,100000082911,100000083037,100000082274,100000081865,100000105889,100000034881,100000033694,100000102848,100000033948,100000037145,100000135710,100000034588,100000035045,100000025949,100000026150,100000025436,100000033878,100000037282,100000037068,100000025371,100000025620,100000025720,100000034474,100000026056,100000043530,100000026430,100000025587,100000209954,100000052196,100000052070,100000052289,100000029828,100000209448,100000052819,100000158310,100000053381,100000057652,100000025048,100000159199,100000144040,100000029932,100000052798,100000024837,100000051217,100000024296,100000100620,100000166289,100000173044,100000058590,100000058643,100000058717,100000058883,100000059015,100000059181,100000059296,100000059323,100000059480,100000059536,100000083521,100000197899,100000058495,100000167887,100000167731,100000197985,100000083433,100000162523,100000197771,100000138892,100000209827,100000062053,100000061898,100000061717,100000061655,100000198481,100000059679,100000152869,100000198244,100000198383,100000184347,100000172764,100000058924,100000156648,100000198198,100000150655,100000061941,100000210036,100000061187,100000061282,100000061348,100000060192,100000060460,100000060652,100000059846,100000061563,100000198598,100000198719,100000198878,100000198638,100000183667,100000168050,100000060821,100000060976,100000061051,100000210136,100000064145,100000064493,100000064553,100000002086,100000016590,100000083985,100000171579,100000198072,100000106811,100000184221,100000210271,100000151065,100000150958,100000064322,100000064298,100000003548,100000017393,100000066418,100000143223,100000067016,100000066937,100000083665,100000066586,100000199077,100000211340,100000016435,100000084046,100000084123,100000084293,100000084321,100000084597,100000136511,100000138980,100000198912,100000170610,100000067664,100000065598,100000067153,100000169286,100000184984,100000066636,100000067477,100000210722,100000199275,100000033755,100000070319,100000070281,100000071353,100000199371,100000085390,100000085195,100000036552,100000069540,100000070426,100000070514,100000085242,100000085787,100000199552,100000145839,100000107470,100000210892,100000210959,100000071238,100000070920,100000071428,100000071756,100000071960,100000096482,100000211458,100000070855,100000096754,100000097033,100000096612,100000096897,100000199497,100000173147,100000173274,100000094720,100000072884,100000072786,100000073140,100000173683,100000096369,100000096587,100000097512,100000073090,100000072643,100000071665,100000097298,100000132245,100000173422,100000211272,100000134990,100000211815,100000073384,100000083329,100000097331,100000100222,100000139144,100000143468,100000143689,100000073222,100000097139,100000139538,100000132378,100000099985,100000136787,100000097788,100000046149,100000211540,100000132560,100000132692,100000184516,100000073560,100000073634,100000071597,100000132874,100000143754,100000136884,100000064943,100000100061,100000072597,100000132777,100000212034,100000211684,100000137697,100000133448,100000083743,100000148799,100000211711,100000139641,100000133569,100000086119,100000085928,100000199183,100000050590,100000148583,100000132998,100000150263,100000150140,100000136496,100000038052,100000212322,100000199622,100000133675,100000097643,100000039490,100000056072,100000042594,100000049753,100000137874,100000070741,100000036071,100000091663,100000065129,100000054254,100000091395,100000137146,100000097450,100000096138,100000006071,100000049230,100000212272,100000002998,100000041761,100000055719,100000035823,100000040280,100000054363,100000040911,100000094678,100000038768,100000094390,100000136020,100000065263,100000055612,100000056151,100000049387,100000062639,100000068620,100000047514,100000054095,100000047263,100000043888,100000039318,100000134118,100000049126,100000073729,100000062742,100000077172,100000041843,100000148645,100000048895,100000072110,100000136364,100000112765,100000112021,100000045720,100000046680,100000105946,100000109281,100000134598,100000063187,100000056419,100000148994,100000148833,100000145167,100000142018,100000199997,100000113395,100000137781,100000137943,100000149062,100000134849,100000149387,100000149153,100000135079,100000135334,100000075721,100000047648,100000015874,100000041053,100000125153,100000142641,100000149591,100000138361,100000138439,100000135414,100000142310,100000135527,100000138611,100000200153,100000110596,100000081332,100000142799,100000125458,100000136130,100000152333,100000152687,100000142949,100000212577,100000138777,100000152526,100000157159,100000200368,100000081287,100000142834,100000152448,100000153297,100000111875,100000151298,100000037336,100000099811,100000112211,100000064092,100000037497,100000074225,100000074123,100000074410,100000073841,100000154722,100000036233,100000144556,100000174267,100000104047,100000073996,100000074386,100000212686,100000110150,100000212722,100000155334,100000076524,100000212830,100000154669,100000157699,100000200470,100000074748,100000212998,100000039071,100000073430,100000155058,100000072052,100000200523,100000078280,100000065995,100000069886,100000154985,100000125291,100000155157,100000137486,100000145286,100000076284,100000098471,100000110343,100000158543,100000076354,100000158256,100000158176,100000104898,100000051556,100000200643,100000081978,100000157767,100000050478,100000050369,100000015149,100000110434,100000157940,100000076412,100000037739,100000110277,100000158068,100000158717,100000200734,100000040727,100000075096,100000046887,100000069285,100000069348,100000075239,100000062277,100000056917,100000186220,100000113260,100000213157,100000200897,100000076920,100000110826,100000213280,100000158677,100000158899,100000201037,100000051120,100000039138,100000162175,100000101592,100000107515,100000161953,100000162091,100000161842,100000159064,100000076657,100000071825,100000158460,100000076789,100000155231,100000070651,100000108268,100000162446,100000162642,100000077045,100000076150,100000047176,100000137334,100000159486,100000162217,100000201114,100000160931,100000069633,100000160269,100000162730,100000163287,100000075362,100000162930,100000213610,100000077982,100000160072,100000003631,100000112855,100000161291,100000163425,100000201233,100000077686,100000077760,100000163083,100000066054,100000201355,100000164969,100000164886,100000165076,100000077581,100000077858,100000137238,100000164750,100000163969,100000164032,100000163693,100000213711,100000079975,100000079479,100000079616,100000078674,100000079034,100000079519,100000079127,100000046731,100000003128,100000040868,100000199754,100000199848,100000200249,100000200052,100000078885,100000002141,100000065844,100000017553,100000213893,100000079793,100000079889,100000078973,100000127797,100000080055,100000201460,100000042832,100000042978,100000048654,100000079215,100000045377,100000046545,100000067918,100000056621,100000069013,100000071036,100000039648,100000043621,100000042259,100000055881,100000055486,100000080828,100000035667,100000122155,100000124670,100000055272,100000057511,100000080262,100000048050,100000036185,100000049957,100000043273,100000122445,100000054860,100000038935,100000041161,100000042077,100000051667,100000041685,100000015923,100000055022,100000105742,100000201542,100000186640,100000057299,100000082748,100000113743,100000201690,100000201865,100000048971,100000201970,100000086375,100000084850,100000084960,100000134626,100000202044,100000054692,100000187283,100000213997,100000084447,100000085019,100000084662,100000085566,100000085639,100000074514,100000085881,100000037984,100000202358,100000051966,100000062895,100000035764,100000062932,100000051786,100000039857,100000036332,100000038877,100000137597,100000202292,100000038513,100000074847,100000076058,100000054949,100000086449,100000086555,100000086616,100000086711,100000165255,100000075133,100000212429,100000186432,100000008451,100000175596,100000011488,100000086291,100000165134,100000048264,100000165446,100000055541,100000166998,100000085448,100000135875,100000087032,100000066723,100000124948,100000041567,100000057359,100000010296,100000140064,100000214087,100000051056,100000086829,100000044983,100000065632,100000037869,100000045936,100000069165,100000079330,100000202133,100000214196,100000087338,100000087419,100000087297,100000046338,100000042792,100000039737,100000134446,100000175845,100000017920,100000109455,100000068265,100000053611,100000113114,100000135182,100000043069,100000196980,100000096945,100000083870,100000087558,100000038325,100000017497,100000134798,100000077217,100000112379,100000068975,100000047065,100000056839,100000200986,100000109774,100000113675,100000005957,100000068382,100000111779,100000053478,100000056718,100000004552,100000048410,100000064687,100000041926,100000087965,100000142197,100000087778,100000087856,100000042331,100000175784,100000015423,100000154019,100000005754,100000169180,100000044615,100000070011,100000086988,100000044084,100000057025,100000044319,100000041276,100000099713,100000063825,100000109836,100000065061,100000087114,100000049048,100000045885,100000047732,100000065482,100000110937,100000054484,100000112686,100000050090,100000052945,100000064837,100000081657,100000136627,100000112551,100000038487,100000039559,100000051428,100000109395,100000054793,100000062348,100000072368,100000124749,100000078427,100000111159,100000044478,100000070119,100000050187,100000087621,100000048732,100000063362,100000088626,100000065768,100000078352,100000088732,100000112456,100000046058,100000088382,100000088459,100000187974,100000131896,100000213096,100000088526,100000045534,100000088020,100000054533,100000169469,100000089592,100000089845,100000089180,100000089689,100000091137,100000089085,100000188126,100000017869,100000088866,100000176148,100000088920,100000110051,100000047355,100000169583,100000078018,100000113885,100000092234,100000051883,100000103428,100000018535,100000066830,100000063988,100000100445,100000108030,100000004089,100000111654,100000111950,100000047487,100000002778,100000012782,100000107766,100000093619,100000155688,100000195282,100000155411,100000157429,100000075831,100000186138,100000214656,100000214596,100000214723,100000155749,100000080388,100000101289,100000187441,100000187546,100000187636,100000187896,100000033582,100000083135,100000034332,100000183328,100000050964,100000163125,100000142265,100000175222,100000090060,100000040573,100000175410,100000175685,100000090191,100000064745,100000089283,100000102998,100000105256,100000141311,100000089427,100000161787,100000108455,100000175930,100000071116,100000089766,100000214368,100000053731,100000187390,100000089358,100000089984,100000175346,100000183777,100000091541,100000012172,100000092691,100000137071,100000105626,100000090240,100000176028,100000176266,100000176379,100000090354,100000090442,100000101695,100000098532,100000156920,100000139418,100000168785,100000182793,100000109035,100000103655,100000057129,100000161447,100000183496,100000183975,100000185490,100000076869,100000187157,100000165328,100000004261,100000175162,100000177691,100000214262,100000189060,100000214462,100000156540,100000178198,100000178861,100000180868,100000190742,100000190843,100000215391,100000003956,100000090599,100000090619,100000090735,100000100560,100000101813,100000139768,100000125358,100000215018,100000214855,100000214932,100000215277,100000215121,100000189511,100000138070,100000101925,100000215444,100000090860,100000091025,100000090924,100000091221,100000149868,100000140658,100000146488,100000174814,100000215537,100000174152,100000174516,100000211035,100000169669,100000113458,100000174068,100000176481,100000003388,100000154215,100000003782,100000001828,100000001956,100000001754,100000003867,100000024058,100000103896,100000215726,100000131928,100000091960,100000092057,100000004699,100000006337,100000006741,100000006865,100000006963,100000007859,100000007039,100000007449,100000007579,100000007644,100000007750,100000007970,100000008065,100000008170,100000007291,100000007384,100000009637,100000009724,100000010071,100000006554,100000006688,100000010165,100000092355,100000010373,100000010486,100000010522,100000010696,100000010721,100000011162,100000011248,100000011385,100000011517,100000011663,100000011736,100000011839,100000011959,100000012071,100000012249,100000012392,100000012465,100000012512,100000012634,100000012888,100000092187,100000092712,100000092910,100000092854,100000091844,100000012948,100000013061,100000013173,100000013252,100000013329,100000013426,100000013525,100000019023,100000007191,100000019167,100000019265,100000019334,100000022088,100000018435,100000018640,100000018744,100000092421,100000216013,100000091461,100000092511,100000136954,100000094452,100000018874,100000094590,100000018975,100000020080,100000020197,100000020217,100000020559,100000020664,100000020781,100000020855,100000020987,100000021031,100000021351,100000021459,100000021542,100000021620,100000021854,100000021946,100000176885,100000173942,100000176555,100000022130,100000022427,100000022864,100000022747,100000022545,100000022632,100000216399,100000216158,100000022946,100000002811,100000002491,100000176780,100000176627,100000021787,100000173812,100000094251,100000094155,100000094090,100000093916,100000093147,100000216286,100000093290,100000174479,100000093488,100000093018,100000093518,100000093864,100000216473,100000093330,100000174364,100000173746,100000219121,100000216532,100000216628,100000177398,100000177018,100000177255,100000177144,100000093781,100000094876,100000189697,100000217539,100000219399,100000176975,100000041450,100000217263,100000095219,100000173599,100000095740,100000177485,100000177574,100000096073,100000096222,100000095967,100000095889,100000217815,100000219215,100000173336,100000177780,100000219548,100000219630,100000219797,100000218082,100000218296,100000217972,100000219830,100000218113,100000189728,100000178353,100000218374,100000219965,100000220294,100000220393,100000220050,100000220157,100000179527,100000189935,100000179438,100000201731,100000220465,100000220516,100000220668,100000220780,100000190237,100000190457,100000179741,100000190358,100000180079,100000218427,100000218667,100000218760,100000220863,100000220996,100000221074,100000221152,100000221223,100000190511,100000190152,100000180660,100000180349,100000218535,100000180483,100000221354,100000190075,100000095630,100000095017,100000094957,100000132155,100000095593,100000095440,100000095327,100000095112,100000180964,100000218870,100000221449,100000189856,100000218997,100000100721,100000180757,100000210434,100000210669,100000210551,100000143551,100000041363,100000047996,100000049566,100000181623,100000219063,100000196788,100000216776,100000216877,100000210360,100000213390,100000181797,100000182027,100000191090,100000133164,100000050293,100000133350,100000190980,100000133279,100000133087,100000209792,100000150350,100000196414,100000211163,100000192132,100000192239,100000211922,100000217068,100000205596,100000215860,100000204083,100000213469,100000205637,100000206021,100000203920,100000217682,100000191118,100000075579,100000192093,100000053967,100000191918,100000091733,100000136265,100000150452,100000086021,100000027458,100000213540,100000027552,100000027628,100000027745,100000027822,100000027962,100000028071,100000028855,100000028998,100000029292,100000029562,100000027166,100000122591,100000182678,100000191217,100000216971,100000191383,100000099171,100000192345,100000217794,100000217185,100000205811,100000205965,100000215919,100000215667,100000196654,100000205762,100000212161,100000048334,100000192491,100000063541,100000192554,100000192620,100000037620,100000045253,100000018144,100000042178,100000106777,100000105427,100000017184,100000168465,100000191459,100000054127,100000042470,100000182216,100000056329,100000045131,100000004486,100000021195,100000221592,100000221631,100000037576,100000088216,100000191551,100000134270,100000015313,100000100198,100000045484,100000040160,100000134386,100000053859,100000221786,100000045058,100000036923,100000088190,100000221868,100000221914,100000055188,100000109956,100000111510,100000192876,100000222032,100000141816,100000191658,100000150578,100000105094,100000192773,100000084737,100000149228,100000145984,100000144667,100000193392,100000194136,100000102248,100000193447,100000193942,100000194287,100000141948,100000191765,100000222161,100000017678,100000193177,100000194035,100000101043,100000193868,100000191835,100000140843,100000150090,100000194488,100000222241,100000077468,100000222335,100000222476,100000135234,100000149449,100000102437,100000125033,100000194755,100000002697,100000104625,100000142490,100000222632,100000099466,100000154153,100000141213,100000103314,100000103052,100000195020,100000146214,100000103567,100000145024,100000140126,100000139344,100000195340,100000043480,100000111438,100000195121,100000066314,100000168961,100000142563,100000111337,100000107229,100000141793,100000144282,100000144449,100000099318,100000134066,100000164293,100000195410,100000153356,100000153417,100000153578,100000153667,100000044596,100000166040,100000150744,100000001278,100000151415,100000145756,100000140923,100000113554,100000015693,100000103783,100000153149,100000152976,100000152781,100000151986,100000102744,100000106244,100000154361,100000002549,100000040699,100000146319,100000103287,100000107816,100000156185,100000154586,100000014950,100000154472,100000106085,100000141034,100000106658,100000149961,100000102171,100000104443,100000107063,100000101321,100000102599,100000146069,100000100924,100000153021,100000100335,100000068567,100000182577,100000145610,100000106153,100000149666,100000141143,100000097983,100000161580,100000155835,100000145356,100000102391,100000108954,100000154865,100000015246,100000222725,100000168691,100000156259,100000069756,100000170960,100000157360,100000170887,100000049633,100000169398,100000170785,100000069930,100000157023,100000055910,100000183132,100000164659,100000164360,100000166131,100000157563,100000157220,100000182837,100000171093,100000166514,100000103135,100000183035,100000169090,100000182990,100000153974,100000153782,100000153837,100000156740,100000156875,100000161346,100000172548,100000172467,100000172388,100000172255,100000172133,100000143147,100000074648,100000183221,100000183570,100000068425,100000159660,100000159239,100000167427,100000159384,100000159519,100000167329,100000159758,100000075446,100000167527,100000167678,100000143360,100000167224,100000172885,100000111080,100000184084,100000081717,100000168182,100000157853,100000141651,100000080464,100000043917,100000184126,100000122251,100000172968,100000052666,100000184473,100000108198,100000104114,100000222997,100000222886,100000183885,100000172662,100000162311,100000179297,100000185053,100000185190,100000185228,100000185383,100000056235,100000160652,100000122335,100000146195,100000184873,100000110741,100000156314,100000184696,100000043738,100000184726,100000168837,100000186356,100000174697,100000185593,100000223026,100000185680,100000185770,100000139862,100000186794,100000144369,100000163391,100000185833,100000185989,100000186080,100000186583,100000068819,100000186925,100000187072,100000223135,100000164430,100000186844,100000139017,100000163725,100000163875,100000163519,100000188049,100000174711,100000187748,100000164156,100000042666,100000188431,100000188745,100000078717,100000112175,100000188972,100000015798,100000188818,100000188554,100000049880,100000017712,100000075697,100000077310,100000188649,100000135965,100000175038,100000003034,100000002316,100000151646,100000141535,100000081026,100000056531,100000062128,100000167928,100000016055,100000074012,100000040095,100000053590,100000189372,100000189433,100000105377,100000108387,100000109663,100000132495,100000188247,100000174939,100000098753,100000035933,100000065329,100000044129,100000188316,100000038684,100000189166,100000109588,100000189289,100000165897,100000063668,100000039243,100000072451,100000222571,100000177817,100000155983,100000178637,100000038299,100000178773,100000043366,100000178523,100000178416,100000178095,100000178247,100000078534,100000045679,100000068110,100000072255,100000048115,100000223278,100000179360,100000112995,100000223351,100000111254,100000177987,100000179611,100000036812,100000179113,100000179083,100000062527,100000178970,100000043192,100000223444,100000179890,100000036746,100000053281,100000179940,100000063032,100000074911,100000038136,100000180511,100000223544,100000005816,100000053184,100000066120,100000180155,100000180226,100000075955,100000181084,100000190629,100000181218,100000050768,100000039973,100000063299,100000223659,100000046451,100000181132,100000181485,100000080574,100000082053,100000165591,100000223760,100000047896,100000005692,100000108535,100000063420,100000181341,100000166862,100000166613,100000181836,100000181946,100000044283,100000181510,100000182159,100000048534,100000167072,100000001136,100000049488,100000125587,100000127674,100000014857,100000193036,100000166722,100000193210,100000192970,100000068096,100000055363,100000113081,100000015584,100000053034,100000195718,100000195825,100000195597,100000046926,100000099249,100000224153,100000195622,100000036480,100000036642,100000078110,100000223921,100000224068,100000223848,100000224415,100000224536,100000195969,100000196143,100000196029,100000196219,100000224243,100000224681,100000224777,100000224833,100000224368,100000224992,100000225038,100000225155,100000225255,100000226094,100000225376,100000063723,100000225563,100000225685,100000225854,100000225744,100000225437,100000109152,100000046225,100000044824,100000066297,100000099682,100000044746,100000062413,100000225967,100000110695,100000226110,100000226282,100000164568,100000226466,100000108766,100000106576,100000226310,100000101171,100000098842,100000104328,100000101758,100000106373,100000226667,100000226787,100000226958,100000226815,100000226595,100000140336,100000098271,100000133864,100000097881,100000124836,100000161627,100000202448,100000000975,100000032743]
j = "/Users/lx/test/100001053122.csv"
with open(j,'r') as rf:
    dd = rf.read()
for i in a:
    name_file = "".join([des_file,str(i),".csv"])
    # print(name_file)
    with open(name_file,'w') as on_s:
        on_s.write(dd)
    # os.mknod(name_file)
# #存储打包下载文件目录
# downloads_file = des_file+"/downloads/"
# #如果打包文件目录不存在则创建
# if not path.exists(downloads_file):
#     os.mkdir(downloads_file)
# #打包下载文件名称
# filename = "10000024325"
# #打包文件地址
# filename_downloads = downloads_file+filename+".zip"
# #如果打包文件存在则先删除
# if path.isfile(downloads_file):
#     os.remove(downloads_file)




#同一天不同商户
# #需要打包的具体文件个数
# # mch_ids= [1,2] #商户id
# # day_s = 1 #具体日期 1号
# # file_list = ["".join(["/",str(day_s),"/",str(i)]) for i in mch_ids] #组合天数
# # des_file_list = [des_file+ i for i in file_list]
# #
# # file_list = ["".join(["/",str(day_s),"日/",str(i)]) for i in mch_ids] #打包显示组合天数
# # des_list = zip(des_file_list,file_list)
#
# #不同商户有日期区间
# mch_ids=[1,2]
# days=[1,2,3]
# # def get_file_list(ss=True):
# #
# #     charac = "/" if ss else "日/"
# #     file_list = ["".join(["/",str(j),charac,str(i)]) for i in mch_ids for j in days] #组合天数
# #     return file_list
#
# file_list , file_with_date= [["".join(["/",str(j),charac,str(i)]) for i in mch_ids for j in days] for charac in ["/","日/"]]
# des_file_list = [des_file+ i for i in file_list]
# des_list = zip(des_file_list,file_with_date)
# print(file_list)
# print(file_with_date)


# with zipfile.ZipFile(filename_downloads, 'w') as zf:
#     # try:
#     for des_file_list, file_list in des_list:
#         zf.write(des_file_list,arcname=file_list)
    # except Exception as err:
    #     log.exception.exception(err)
    # finally:
    #     zf.close()


# def get_date_range(create_at_start, create_at_end):
#     count = (datetime.datetime.strptime(str(create_at_end), "%Y-%m-%d") -
#              datetime.datetime.strptime(str(create_at_start), "%Y-%m-%d")).days
#     create_at_end_date = datetime.datetime.strptime(
#         str(create_at_end), "%Y-%m-%d")
#     return [datetime.datetime.strftime(create_at_end_date - datetime.timedelta(i), "%Y-%m-%d") for i in
#             range(count + 1)]
#
# r = get_date_range("2017-07-13","2017-07-13")
# print(sorted(r))
#
# all_day_csv = []
# for i in r:
#     year_e, month_e, day_e = i.split("-")
#     day_file_mch = [
#         "".join(["/", str(year_e), "/", str(int(month_e)), "/", str(int(day_e)), "/", str(i), ".csv"]) for
#         i in ["10000000"]]
#     all_day_csv.append(day_file_mch)
# print(all_day_csv)


