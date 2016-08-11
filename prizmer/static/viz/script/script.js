var mainframeElement;
var errorElement;
var modalWindow;
var refreshmentTime;
var dataTableColumnNumber = 12;

var mainTimer;

function InitScript(){
    errorElement = document.getElementById('errordiv');
    mainframeElement = document.getElementById('mainframe');
	modalWindow =  document.getElementById('modal_form');
	
	if (mainframeElement == null || modalWindow == null || errorElement==null){
		alert('Can\'t get link to HTML object');
	}else{
		SetEnvironment();			
	}
}

function setMainframeSize(width, height){
    mainframeElement.style.width = width + 'px';
    mainframeElement.style.height = height + 'px';
}

function setMainframePosition(left, top){
    mainframeElement.style.left = left + 'px';
    mainframeElement.style.top = top + 'px';
}

function setBackgroundImage(imgname){
	//mainframeElement.style.backgroundImage = "url(images/"+imgname+")";
    mainframeElement.style.backgroundImage = "url(../../static/viz/images/"+imgname+")";
}

function getIntFromPxStr(str){
	try {
		return parseInt(str.substring(0, str.indexOf('px')));
	}catch(ex){
		alert('getIntFromPxStr: ' + ex);
	}
}

function SetEnvironment(){
	$.get(
	  //"sendJSON.php",
      "/viz/viz_mainframe",
	  {queryType: 1},
	  function(data){
          /*проверка на автоматическое преобразование браузером*/
          var dataType = typeof(data);
          var d;
          if (dataType == 'string')
              d = $.parseJSON(data);
          else
              d = data;

          //служебный флаг вывода чистого JSON
          var showRawJSON = false;
          if (showRawJSON){
              errorElement.innerHTML = data;
              clearInterval(mainTimer);
          }

		if (d)
		{
			try {
                //период отправки запроса на получение значений серверу
				refreshmentTime = parseInt(d.refreshmentTimeMS);

                //установка статичных параметров
				setMainframeSize(d.mainframewidth, d.mainframeheight);
				setMainframePosition(d.mainframeleft, d.mainframetop);
				setBackgroundImage(d.backgroundurl);
                createDataTable(dataTableColumnNumber);

                //сразу получим значения с сервера (не дожидаясь начала работы таймера)
                GetValuesFromServer();

				if (refreshmentTime)
					mainTimer = setInterval(GetValuesFromServer, refreshmentTime);


			}catch(ex){
				alert(ex);		
			}
		} else {
               errorElement.innerHTML = 'SetEnvironment: Ошибка парсинга JSON ' +
                'строки при получении значений с сервера';
		}
	  }
	);	
}

var incomingData;
function GetValuesFromServer(){
    $.get(
        //"sendJSON.php",
        "/viz/viz_devices",
        {queryType: 2},
        function(data){
            var dataType = typeof(data);
            var d;
            if (dataType == 'string')
                d = $.parseJSON(data);
            else
                d = data;

            //служебный флаг вывода чистого JSON
            var showRawJSON = false;
            if (showRawJSON){
                errorElement.innerHTML = data;
                clearInterval(mainTimer);
            }


            if (d){
                incomingData = d;
                for (var device in d){
                    var curDev = d[device];
                    placeDivOnMainPage(device,"mainframeValueBox",
                        {left:curDev.deviceboxleft, top:curDev.deviceboxtop},
                        {width:curDev.deviceboxwidth, height:curDev.deviceboxheight});
                    var vals = curDev.values;

                    for (var val in vals){
                        var curVal = vals[val];
                        if (curVal.showonmain) {
                            var valueID = device + '_' + val;
                            placeDivOnMainPage(valueID,'mainframeValue',
                                {left:curVal.mvalleft, top:curVal.mvaltop},
                                {width:60, height:20});
                            setDivProperty(valueID, curVal.value, curVal.color);
                        }
                    }
                    if (selectedDeviceId)
                        fillDataTable(d[selectedDeviceId].values);
                }
                eventBinder();
            } else{
                errorElement.innerHTML = 'GetValuesFromServer: Ошибка парсинга JSON ' +
                'строки при получении значений с сервера';
            }
        }
    );
}

var setEventFlag = true;
function eventBinder(){
    if (setEventFlag){
        $('.mainframeValueBox').on("click", showModalWindow);
        $('#modal_close').on("click", closeModalWindow);
    }
    setEventFlag = false;
}

function placeDivOnMainPage(id,cssclassname,position,size){

    if (document.getElementById(id) == null){
        var valDiv = document.createElement('div');
        valDiv.id = id;
        valDiv.className = cssclassname;
        valDiv.style.left = position.left + 'px';
        valDiv.style.top = position.top + 'px';
        valDiv.style.width = size.width + 'px';
        valDiv.style.height = size.height + 'px';

        mainframeElement.appendChild(valDiv);

    }
}

function getValWithoutComma(valWithComma){
    var tmpVal = valWithComma.toString();

    if (tmpVal.indexOf(',') != -1) {
        tmpVal = tmpVal.replace(',', ' ');
    }

    return tmpVal;
}

function setDivProperty(id, value, color){
    var curDiv = document.getElementById(id);
    try{
        curDiv.innerHTML = getValWithoutComma(value);
        curDiv.style.color = color;
    }catch(ex){
        alert('setDivValue: ' + ex);
    }
}

/*в зависимости от значения показывает или скрывает обводку вокруг
 выбранного прибора*/
function selectDevice(selectedDeviceId, doShow){
    try{
        if (doShow){
            var left = incomingData[selectedDeviceId].deviceboxleft;
            var top = incomingData[selectedDeviceId].deviceboxtop;
            var width = incomingData[selectedDeviceId].deviceboxwidth;
            var height = incomingData[selectedDeviceId].deviceboxheight;

            $('#device_overlay').css({'left': left, 'top': top, 'width': width, 'height' : height});
            $('#device_overlay').css('display','block');
        }else{
            $('#device_overlay').css('display','none');
        }
    }catch (ex)
    {
        alert('selectDevice: Блок обводки недоступен');
    }
}

var selectedDeviceId = null;
function showModalWindow(){

	//event.preventDefault(); // выключаем стандартную роль элемента

    selectedDeviceId = $(this).attr('id');
    fillDataTable(incomingData[selectedDeviceId].values);

    selectDevice(selectedDeviceId, true);
	//$('#overlay').css('width',mainframeElement.style.width);				
	//$('#overlay').css('display','block');
					
	$('#modal_form').css('top',0);
	$('#modal_form').css('left', 0);					
	$('#modal_form').css('width', mainframeElement.style.width);
	$('#modal_form').css('height','60px');	
	$('#modal_form').css('display', 'block').animate({opacity: 1}, 100); 
}

function closeModalWindow(){
    selectedDeviceId = null;
    clearDataTable();

	$('#modal_form').css('display', 'none'); // делаем ему display: none;
	$('#overlay').css('display', 'none'); // скрываем подложку

    selectDevice(selectedDeviceId, false);
}

function getPropertiesNumber(obj){
    return Object.keys(obj).length;
}


var createDataTableFlag = true;
function createDataTable(columnNumber){
    if (createDataTableFlag){
        var dtable = document.createElement('table');
        dtable.id = 'datatable';
        document.getElementById('modal_form').appendChild(dtable);

        var dtableref = document.getElementById('datatable');
        var r1 = document.createElement('tr'); r1.id = 'tablerow1';
        var r2 = document.createElement('tr'); r2.id = 'tablerow2';
        dtableref.appendChild(r1);
        dtableref.appendChild(r2);

        var r1ref = document.getElementById('tablerow1');
        var r2ref = document.getElementById('tablerow2');

        for (var i=1; i <= columnNumber; i++) {
            var th = document.createElement('th');
            th.id = 'tcap' + i;
            var td = document.createElement('td');
            td.id = 'tval' + i;
            r1ref.appendChild(th);
            r2ref.appendChild(td);
        }
        createDataTableFlag = false;
    }
}

function fillDataTable(deviceValues){
    if (document.getElementById('datatable')){
            try{
                clearDataTable();
                var i = 1;
                for (var val in deviceValues){
                    var curVal = deviceValues[val];
                    document.getElementById('tcap' + i).innerHTML = getValWithoutComma(curVal.caption);
                    document.getElementById('tval' + i).innerHTML = getValWithoutComma(curVal.value);
                    document.getElementById('tval' + i).style.color = curVal.color;
                    i++;
                }
            }catch(ex){
                alert('fillDataTable: ' + ex);
            }
    }
}

function clearDataTable(){
    var tableElem = document.getElementById('datatable');
    if (tableElem){
        var cells = document.getElementById('datatable').rows[0].cells.length;
        for (var i = 1; i <= cells; i++){
            document.getElementById('tcap' + i).innerHTML = '';
            document.getElementById('tval' + i).innerHTML = '';
            document.getElementById('tval' + i).style.color = 'Black';
        }
    }
}
