import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import QtMultimedia 5.8
//import QtQuick.Particles 2.11
import "./trigonometryLogic.js" as Logic



Item {
    id: main
    property real radius: main.width/2
    property int sliceIndex: 0
    property var soundList : []

    function show(index) {
          soundList.itemAt(index).effect.play();
          console.log(index);
          list.itemAt(index).visible= true;
          noLight.visible= false;


        }
    function hide(index){
        noLight.visible= true;
        list.itemAt(index).visible= false;


    }
    
    
    Connections {
        target: myPad
        onPlayPadOn: {

            var index = myPad.getNum();
            show(index);
        }
        onPlayPadOff: {
            var index = myPad.getNum();
            hide(index)
        }

    }

    Image{
        id:noLight
        anchors.fill: parent
        anchors.margins : 5
        source : "./Images/Pie_" + 4 + ".png"
        fillMode: Image.PreserveAspectFit
        visible: true
    }
    
    Repeater{
        id: list
        model: 4
        Image{
            anchors.fill: parent
            anchors.margins : 5
            source : "./Images/Pie_" + index + ".png"
            fillMode: Image.PreserveAspectFit
            visible: false
        }


    }

    Repeater{
        id: soundList
        model: 4
        Item{
            property alias effect: mysound
                SoundEffect {
                    id:mysound
                     source: "./Sounds/Effect_" + index + ".wav"
                 }
        }
    }




    

    Image{
        id:allLight
        anchors.fill: parent
        anchors.margins : 5
        source : "./Images/Pie_" + "full" + ".png"
        fillMode: Image.PreserveAspectFit
        visible: true
        opacity: 0.0

        Connections {
            target: myPad
            onLightUp: {               // this is the lightUp() function defined in pad.h
                lightUpAnime.running = true;
            }
            onLightDown: {               // this is the lightUp() function defined in pad.h
                lightUpAnime.running = false;
            }
        }

        SequentialAnimation{
            id:lightUpAnime

            NumberAnimation {
                target: allLight
                property: "opacity"
                from:0.0
                to:1.0
                duration: 150
                easing.type: Easing.InOutQuad
            }
            NumberAnimation {
                target: allLight
                property: "opacity"
                from:1.0
                to:0.0
                duration: 150
                easing.type: Easing.InOutQuad
            }

            running: false
        }
    }


    MultiPointTouchArea {
            anchors.fill: parent
            maximumTouchPoints: 1
            touchPoints: [
                TouchPoint {
                    id: container
                    //property ParticleSystem system
                    onPressedChanged: {
                        if (pressed) {
                            var number = Logic.coordinatetoIndex(x,y);

                            show(number)
                            myPad.pressed(number);

                        }

                        else{
                            var number2 = Logic.coordinatetoIndex(x,y);
                            hide(number2)
                        }
                    }
                }
            ]
        }

}
