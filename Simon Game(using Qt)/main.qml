import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2


Window {
    visible: true
    title: qsTr("Hello Simon")
    width:300
    height: 600

    Column{
        anchors.fill: parent

        SimonGame {
            id: simonGame
            width: parent.width
            height: parent.height * 0.8
        }

        PlayButton {
            id: bouton
            anchors.horizontalCenter: parent.horizontalCenter
        }


        GameOverText {
            id: gameOver
            //x:100
            y:210
            scale:0.0

            Connections {
                target: myPad
                onGameOver: {               // this is the lightUp() function defined in pad.h
                    gameOverAnime.running = true;
                }
                onGameStart: {               // this is the lightUp() function defined in pad.h

                    gameOverAnime.running = false;
                    gameOver.scale=0.0;
                }
            }


            NumberAnimation {
                id: gameOverAnime
                target: gameOver
                property: "scale"
                from:0.0
                to:1.0
                duration: 200
                easing.type: Easing.InOutQuad
                running:false
            }



        }

    }





}
