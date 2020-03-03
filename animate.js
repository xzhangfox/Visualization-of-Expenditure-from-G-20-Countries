var myImage = document.getElementById("mainImage");

var imageArray = ["style/cover.jpg","style/cover1.jpg", "style/cover2.png", "style/cover3.jpg"];

var imageIndex = 0;

function changeImage() {
    myImage.setAttribute("src", imageArray[imageIndex]);
    imageIndex++;
    if (imageIndex >= imageArray.length) {
        imageIndex = 0;

    }
}

var intervalHandle = setInterval(changeImage, 2180);

myImage.onclick = function() {

    clearInterval(intervalHandle);
}


