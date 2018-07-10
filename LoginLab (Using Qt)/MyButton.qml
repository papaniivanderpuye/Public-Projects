import QtQuick 2.9
import QtQuick.Window 2.2

Image {
    id: myButton
    source: "./images/bluebutton.png"
    // Everytime "button is pressed, since this is bound to scale,
    // it scales it as well as handle other onButtonPress activities
    scale: mouseAreaLogin.pressed ? 0.9 : 1
    property alias imageSource: myImage.source
    property alias buttonText: myText.text
    signal buttonPressed()

    Image {
        id: myImage
        source: "./images/login.png"
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        anchors.leftMargin: 80
    }
    
    Text {
        id: myText
        text: qsTr("Login")
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font {
            family: "Helvetica"
            pixelSize: parent.width * 0.07
        }
        color: "white"
    }
    
    MouseArea {
        id: mouseAreaLogin
        anchors.fill: parent
        onClicked: {
            buttonPressed()
        }
    }
}
