#include "counter.h"

#include <QFile>
#include <QTextStream>
#include <QDebug>

Counter::Counter(QStringList args1, bool c1 , bool w1 , bool l1,QObject *parent) : QObject(parent)
{
    args = args1;
    c =c1;
    w =w1;
    l =l1;

}

int Counter::wordCount(QString text){

    QString simplified = text.simplified();
    QStringList listOfWords = simplified.split(' ',QString::SkipEmptyParts);
    int numberOfWords = listOfWords.count();

    return numberOfWords;
}

int Counter::lineCount(QString &text){
    QStringList listOfLines = text.split('\n');
    int numberOfLines = listOfLines.count() -1;

    return numberOfLines;
}

int Counter::characterCount(QString &text){
    QString simplified = text.simplified();
    QString characters = simplified.replace(" ","");
    int numberOfChar = characters.length();

    return numberOfChar;
}


void Counter::update(const QString& str){

    Q_UNUSED(str)

    

    foreach (const QString& fileName, args){

        QString text;
        QFile file(fileName);

        if(file.open(QIODevice::ReadOnly)){
            QTextStream stream(&file);
            text = stream.readAll();

            QString header = QString("\n--Count for " ) + fileName+ QString("--" );
            qDebug () << header;

            if(c){
                QString output = QString("Characters: ") + QString::number(characterCount(text));
                qDebug() << output;
            }

            if(w){
                QString output = QString("Words: ") + QString::number(wordCount(text));
                qDebug() << output;
            }

            if(l){
                QString output = QString("Lines: ") + QString::number(lineCount(text));
                qDebug() << output;
            }
        }
    }
}
