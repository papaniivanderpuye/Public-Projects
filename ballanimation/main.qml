import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")


    Image {
        id: ball
        source: "ball.png"
        //anchors.centerIn: parent
        smooth: true
        x : 0
        y:400

        NumberAnimation {
            id:numanim
            target: ball
            property: "x"
            from:10 ; to :550;
            duration: 1000
            running: false
        }



        RotationAnimation on rotation{
            id:rotanim
            from: 45; to: 800
            direction: RotationAnimation.Clockwise
            duration: 900
            running: false

        }

        SequentialAnimation{
            id: sequence;
            NumberAnimation {
                target: ball
                property: "y"
                from:400 ; to :100;
                duration: 300
            }

            NumberAnimation {
                target: ball
                property: "y"
                from:100 ; to :400;
                duration: 300

                //easing.type: "OutExpo"
            }

            NumberAnimation {
                target: ball
                property: "y"
                from:400 ; to :200;
                duration: 250

                //easing.type: "OutExpo"
            }

            NumberAnimation{
                target: ball
                property: "y"
                from:200 ; to :400;
                duration: 250

                //easing.type: "OutExpo"
            }

        running: false
        }



        MultiPointTouchArea{

            anchors.fill:parent
            touchPoints: [
                TouchPoint {
                    id:point1;
                    onPressedChanged: {
                        if (pressed){
                            sequence.running =true;
                            numanim.running =true;
                            rotanim.running=true;
                        }


                }
            }
            ]
        }

    }



}
