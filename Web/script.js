var car_imgArray = new Array();
var bus_imgArray = new Array();
var cat_imgArray = new Array();
var dog_imgArray = new Array();
var ship_imgArray = new Array();

	for(var i=0; i<=190; i++){
		car_imgArray[i] = "images1/test/car/car (" +(i+1)+ ").jpg";
		bus_imgArray[i] = "images1/test/bus/bus (" +(i+1)+ ").jpg";
		cat_imgArray[i] = "images1/test/cat/cat (" +(i+1)+ ").jpg";
		dog_imgArray[i] = "images1/test/dog/dog (" +(i+1)+ ").jpg";
		ship_imgArray[i] = "images1/test/ship/ship (" +(i+1)+ ").jpg";
	}

	function showImage(){
		var objImg = new Array();
		for(var i=0; i<9; i++){
			objImg[i] = document.getElementById("introImg" + i);
		}

		var img_src;
		for(var i=0; i<9; i++){
			var rand = Math.round(Math.random()*4);
			var imgNum = Math.round(Math.random()*190 + 1);
			if(rand == 1){
				img_src = car_imgArray[imgNum];
			}
			else if(rand == 2){
				img_src = bus_imgArray[imgNum];
			}
			else if(rand == 3){
				img_src = dog_imgArray[imgNum];
			}
			else if(rand == 4){
				img_src = cat_imgArray[imgNum];
			}
			else {
				img_src = ship_imgArray[imgNum];
			}
			objImg[i].src = img_src;
		}
}
