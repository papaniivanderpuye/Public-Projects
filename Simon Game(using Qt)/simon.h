#ifndef SIMON_H
#define SIMON_H

#include <QObject>
#include <QTimerEvent>
#include <QTimer>

class Simon : public QObject
{
    Q_OBJECT

public:
    explicit Simon(QObject *parent = nullptr);

    Q_INVOKABLE bool verify();


signals:


private slots:

private:

};

#endif // SIMON_H
