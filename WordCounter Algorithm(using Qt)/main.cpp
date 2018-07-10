#include <QCoreApplication>
#include <QString>
#include <QStringList>
#include <QFile>
#include <QIODevice>
#include <QDebug>
#include <QCommandLineParser>
#include <QCommandLineOption>
#include <QObject>
#include <QFileSystemWatcher>
#include "counter.h"

int main(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);
    QCommandLineParser parser;

    parser.addPositionalArgument("input",QCoreApplication::translate("main","input file containing words"));
    parser.addHelpOption();
    parser.addVersionOption();

    QCommandLineOption countingWords(QStringList() << "w",QCoreApplication::translate("main","count words"));
    parser.addOption(countingWords);

    QCommandLineOption countingLines(QStringList() << "l",QCoreApplication::translate("main","count lines"));
    parser.addOption(countingLines);

    QCommandLineOption countingChar(QStringList() << "c",QCoreApplication::translate("main","count characters"));
    parser.addOption(countingChar);

    parser.process(app);

    const QStringList args = parser.positionalArguments();



    bool c= false;
    bool w= false;
    bool l= false;
    if(parser.isSet(countingChar)){
        c = true;
    }
    if(parser.isSet(countingWords)){
        w = true;
    }
    if(parser.isSet(countingLines)){
        l = true;
    }

    QFileSystemWatcher watcher;
    QString path = "/home/dev/wordCounterPapa";
    if(watcher.addPath(path)){

        qDebug() << QString("working ");
    }


    Counter counter(args,c,w,l);

    //counter.update();


    QObject::connect(&watcher, SIGNAL(directoryChanged(QString) ), &counter, SLOT(update(QString)));

    //

    //QObject::connect( &watcher, SIGNAL(directoryChanged(QString)),&counter, SLOT(update(QStringList,bool,bool,bool)) );



}
