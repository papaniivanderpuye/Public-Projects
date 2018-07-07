import QtQuick 2.7
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2

Button{
    id: button
    text:"Play"

    onClicked: {
        myPad.startAgain();
    }
}
