#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include "stdio.h"
#include "simon.h"
#include <qqml.h>
#include <pad.h>
#include <QList>
#include <QDebug>


int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    //qmlRegisterType<Pad>("CustomComponents",1,0,"Pad");


    // QObject *pad = object->findChild<QObject*>("gamepad");
    //pad->setProperty("color", "red");

    //QObject::connect(&pad,QObject::lightUp, &pad,  )


    Pad myPad;
    engine.rootContext()->setContextProperty("myPad", &myPad);// first letter of name has to be lower case

    engine.load(QUrl(QLatin1String("qrc:/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    //QList<int> sequenceList= {0,1,2,3};
    //qDebug() << "before";
    //myPad.simonSays(sequenceList);
    //qDebug() << "after";









    return app.exec();
}
