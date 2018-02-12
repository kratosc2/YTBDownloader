var player = document.getElementById('aplayer');
player.addEventListener("timeupdate", updateplayer, false);
var nowplay = document.getElementById('nowplay');
var lock = false;
var tn = 0;
function play(d){
	if (tn > 0){
	var before = document.getElementsByName(tn)[0].id;
        document.getElementById(before).style.borderRadius = "5px";
        document.getElementById(before).style.backgroundColor = "green";
	}
	var nametrack = document.getElementById(c).getAttribute('href');
	var na = document.getElementById(c).getAttribute('name');
	var player = document.getElementById('aplayer');
	nowplay.innerHTML = nametrack + (' Now Playing...');
        player.src = c;
	tn = na;
        player.load();
        player.play();
	document.getElementById(d).style.borderRadius = "5px";
	document.getElementById(d).style.backgroundColor = "gold";

}
function loophov(){
	document.getElementById('loop').style.backgroundColor = "gold";
	document.getElementById('loop').style.borderRadius="30%";
}
function loophovout(){
	if (player.loop == false){
	 document.getElementById('loop').style.backgroundColor = "transparent";
         document.getElementById('loop').style.borderRadius="0%";
	}
}
function loop(){
	if (player.loop == false){
		player.loop =true;
        	document.getElementById('loop').style.backgroundColor = "gold";
        	document.getElementById('loop').style.borderRadius="30%";
	}
	else{
         	document.getElementById('loop').style.backgroundColor = "tansparent";
         	document.getElementById('loop').style.borderRadius="0%";
		player.loop = false;
	}
}



function funcstart(){
	lock = true;

}

function funcstop(){
	lock = false;
}
function func(event){
    if (lock == true){
	var player = document.getElementById('aplayer');
	var duration = player.duration;	
    	var divw = document.getElementById('duratline').offsetWidth;
    	var div2 = document.getElementById('point');
    	var pos = event.clientX - 8;
	var sperc = parseInt(pos / (divw/100));
	var sdurat = parseInt(duration* (sperc/100));
	player.currentTime = parseInt(sdurat) - 15;

	}
}
function playb(){
  var player = document.getElementById("aplayer");
  if (player.paused){
    var btn = document.getElementById("ply");
    btn.src = "http://94.54.178.57/pause.png";
    player.play();

  }
  else{
    var btn = document.getElementById("ply");
    btn.src = "http://94.54.178.57/play.png";
    player.pause();
  }

}


var duratline = document.getElementById('duratline');
duratline.addEventListener("click",getpos);

function getpos(event){
  var re = document.getElementById('duratline').getBoundingClientRect();
  var he = document.getElementById("point");
  var x = event.clientX - re.left;
  var player = document.getElementById("aplayer");
  var durat = player.duration;
  var y = document.getElementById('duratline').offsetWidth
  var re = document.getElementById('duratline').getBoundingClientRect();
  var z = x / (y/100);
  player.currentTime = durat * (z/100);

  player.play();

}


vol.addEventListener("click",volumechng);
function volumechng(event){
	var player = document.getElementById('aplayer');
	var voldiv = document.getElementById('volpoint');
	var offset = document.getElementById('vol').offsetWidth;
	var x = event.clientX ;
	var point = offset / offset;
	var vol = x / offset;
	var s = screen.width - 35 - 200;
	var rect = voldiv.getBoundingClientRect();
	var vol = (parseFloat(x-rect.left)/offset)  ;
	voldiv.style.width = x - rect.left + 'px';
	player.volume = vol;
}
function muteb(){
  var player = document.getElementById("aplayer");
  
if (player.volume == 1){
  var pointvol = document.getElementById("volpoint");
  pointvol.style.width = 0 + "%";
  player.volume = 0;
  var btnna = document.getElementById("mutebtn");
  btnna.src = "http://94.54.178.57/mute.png";
}
  else{
    var pointvol = document.getElementById("volpoint");
    pointvol.style.width = 100 +"%";
    player.volume = 1;
    var btnna = document.getElementById("mutebtn");
    btnna.src ="http://94.54.178.57/loud.png";
  }
}



var lockhover = false;

function oth(){


}

function selecthov(event){	
	lockhover = true;
	var offset = document.getElementById('duratline').offsetWidth;
	var player = document.getElementById('aplayer');
	var duration = player.duration;
	var durationline = document.getElementById('duratline');
	var pointerhov = document.getElementById('point');
	var timer = document.getElementById('time');
	var rect = durationline.getBoundingClientRect();
	var x = event.pageX - rect.left;
	var y = event.pageY - 79;
	if (x < 0){
		x = 0
	}
	var ap = durationline.offsetWidth;
	var sperc = x/(offset/100) ;
	var sstime = duration * (sperc/100);
	var curr = 100 * (player.currentTime / duration);
	var secs = parseInt(sstime % 60);
	var mins = parseInt(sstime / 60 );
	if (secs < 10){
		secs = '0' + secs;
	}
	document.getElementById('tooltipid').style.top = y + 30 + 'px';
	document.getElementById('tooltipid').style.left = x + 60 + 'px';
	document.getElementById('tooltipid').innerHTML = mins +':' +secs + ' ';
	document.getElementById('tooltipid').style.opacity = "1";
	if (curr * 2 > sstime){
		pointerhov.style.background = "linear-gradient(to right,seagreen "+(sperc + 1)+"%,gold "+sperc+"%,gold "+(curr + 1)+"%,gold "+sperc+"%,  gold "+sperc+"%,green "+sperc+ "%)";
        	pointerhov.style.transition = "1s";

	}
	else{
	pointerhov.style.background = "linear-gradient(to right,seagreen "+curr+"%,gold "+(curr + 1)+"%,gold "+sperc+"%,  gold "+sperc+"%,green "+sperc+ "%)";
	pointerhov.style.transition = "1s";
	}

}

function outhover(){
	lockhover = false;
	var pointerhov = document.getElementById('point');
	pointerhov.style.background = "white";
        document.getElementById('tooltipid').style.opacity = "0";

}

function updateplayer(){
        var player = document.getElementById("aplayer");
        var point = document.getElementById("point");
        var duration = player.duration;
        var percent = 100 * (player.currentTime / duration);
        var time = document.getElementById("time")
        var secs = parseInt(player.currentTime % 60);
        var secstomin = parseInt(player.currentTime);
	var timeend = document.getElementById('timed');
	var durationmin = parseInt(player.duration / 60);
	var durationsecs = (player.duration % 60);
	timeend.innerHTML = parseInt(durationmin) + ':' + parseInt(durationsecs);
  if (secs < 10){
    secs = "0" + secs
  }

  var mins = parseInt(secstomin / 60);

  time.innerHTML = mins + ":" + secs ;
        if (lockhover == false){
  point.style.background = "linear-gradient(to right, seagreen "+percent+"%,darkgreen "+percent+ "%)";

        }
}

var ars = document.getElementById('lasttrack');
ars = ars.getAttribute('data');

function nextrack(){
	var before = document.getElementsByName(tn)[0].id;
	document.getElementById(before).style.borderRadius = "5px";
        document.getElementById(before).style.backgroundColor = "green";
	var nowplayid = document.getElementById('nowplay');
	var nextdata = parseInt(parseInt(tn)+ 1);
	var player = document.getElementById('aplayer');
	if (ars == tn){
		next = document.getElementsByName(1)[0].id;
		nowplayid.innerHTML = document.getElementById(next).getAttribute('href')+' Now Playing ...' ;
		player.src = next;
		player.load();
		player.play();
		document.getElementById(next).style.borderRadius = "5px";
        	document.getElementById(next).style.backgroundColor = "gold";
        	document.getElementById(next).style.transition = "1s";
		tn = 1;
	}
	else {
	var next = document.getElementsByName(nextdata)[0].id;
	nowplayid.innerHTML = document.getElementById(next).getAttribute('href')+' Now Playing ...' ;
	player.src = next;
	player.load();
	player.play();
	tn = parseInt(tn) + 1;
        document.getElementById(next).style.borderRadius = "5px";
        document.getElementById(next).style.backgroundColor = "gold";
	document.getElementById(next).style.transition = "1s";
	}
}

