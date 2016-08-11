<?php
$qType = $_GET['queryType'];

	if ($qType == 1) {
		$arr = array(
			'refreshmentTimeMS' => 1000,
			'mainframeleft'=> 40,
			'mainframetop' => 40,
			'mainframewidth' => 800,
			'mainframeheight' => 600,
			'backgroundurl' => 'background.png',
		);	
		echo json_encode($arr);
	} else if ($qType == 2) {
		$arr = array(
					'device1' => array(
						'deviceboxleft' => 240,
						'deviceboxtop' => 120,
						'deviceboxwidth' => 70,
						'deviceboxheight' => 60,
                        'values'=> array(
                            'val1' => array(
                                'caption' => 'Voltage',
                                'value' => '219 V',
                                'color' => 'Red',
                                'showonmain' => 0,
                                'mvalleft' => 320,
                                'mvaltop' => 120
                            ),
                            'val2' => array(
                                'caption' => 'T1',
                                'value' => rand(27 , 28) .' C',
                                'color' => 'Green',
                                'showonmain' => 1,
                                'mvalleft' => 200,
                                'mvaltop' => 100
                            )
                        )
					),
					'device2' => array(
						'deviceboxleft' => 345,
						'deviceboxtop' => 280,
						'deviceboxwidth' => 100,
						'deviceboxheight' => 100,
                        'values' => array(
                            'val1' => array(
                                'caption' => 'Voltage',
                                'value' => /*rand(219 , 220) .' V'*/2000000000,
                                'color' => 'Red',
                                'showonmain' => 0,
                                'mvalleft' => 0,
                                'mvaltop' => 0
                            ),
                            'val2' => array(
                                'caption' => 'TCPU',
                                'value' => rand(45 , 47).' C',
                                'color' => 'Green',
                                'showonmain' => 0,
                                'mvalleft' => 0,
                                'mvaltop' => 0
                            ),
                            'val3' => array(
                                'caption' => 'TGPU',
                                'value' => rand(75 , 78).' C',
                                'color' => 'Black',
                                'showonmain' => 0,
                                'mvalleft' => 0,
                                'mvaltop' => 0
                            ),
                            'val4' => array(
                                'caption' => 'FAN1',
                                'value' => rand(800 , 802).' rpm',
                                'color' => 'Blue',
                                'showonmain' => 0,
                                'mvalleft' => 0,
                                'mvaltop' => 0
                            )
                        )
					)										
				);

		echo json_encode($arr);		
	}






