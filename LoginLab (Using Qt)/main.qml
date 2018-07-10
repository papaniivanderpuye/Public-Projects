import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Login Window")

    function debug(name)
    {
        console.log (name, " is pressed")
    }

    Image {
        id: background
        source: "./images/bluebackground.png"
        anchors.fill: parent
    }

    MyButton {
        id: loginButton
        anchors.topMargin: background.height / 3
        anchors.bottom: background.verticalCenter
        anchors.bottomMargin: 25
        anchors.left: background.left
        anchors.leftMargin: 150
        anchors.right: background.right
        anchors.rightMargin: 150
        anchors.top: background.top
        imageSource: "./images/login.png"
        buttonText: "Login"
        onButtonPressed: {
            myBusinessLogic.login()
//            if (loader_MyButton.status === Loader.Null)
//                loader_MyButton.sourceComponent = component_MyButton
//            else
//                loader_MyButton.sourceComponent = undefined

        }

        onButtonTextChanged: {

        }

        // good for initialization of this button, i.e., debug
        Component.onCompleted: {

        }

        // Get a signal from C++ to do something on the screen
        Connections {
            target: myBusinessLogic
            onMySignal: {               // this is the mySignal() function defined in businesslogic.h
                console.log(MyList)
            }
        }
    }

    // TODO: Move position bindings from the component to the Loader.
    //       Check all uses of 'parent' inside the root element of the component.
    Component {
        id: component_MyButton
        MyButton {
            imageSource: "./images/signout.png"
            buttonText: "Sign Out"
            onButtonPressed: {
                myBusinessLogic.signOut()
            }
        }
    }
    Loader {
        id: loader_MyButton
        anchors.bottom: background.bottom
        anchors.bottomMargin: background.height / 3
        anchors.top: background.verticalCenter
        anchors.topMargin: 25
        anchors.left: background.left
        anchors.leftMargin: 150
        anchors.right: background.right
        anchors.rightMargin: 150
        sourceComponent: myBusinessLogic.loaded ? component_MyButton : undefined
    }


}
