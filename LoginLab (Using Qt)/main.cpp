#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include "businesslogic.h"

int main(int argc, char *argv[])
{
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);

    QGuiApplication app(argc, argv);

    BusinessLogic myBusiness;

    QQmlApplicationEngine engine;

    engine.rootContext()->setContextProperty("myBusinessLogic", &myBusiness);// first letter of name has to be lower case

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}
