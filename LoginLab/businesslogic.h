#ifndef BUSINESSLOGIC_H
#define BUSINESSLOGIC_H

#include <QObject>

class BusinessLogic : public QObject
{
    Q_OBJECT

    Q_PROPERTY(bool loaded READ loaded WRITE setLoaded NOTIFY loadedChanged)
    bool m_loaded;

public:
    explicit BusinessLogic(QObject *parent = nullptr);
    Q_INVOKABLE void login();   // function calls so QML can call
    Q_INVOKABLE void signOut();

bool loaded() const;

signals:
    void mySignal(QStringList MyList); // All Q_INVOKABLE, all signals has to be declared lower case

    void loadedChanged(bool loaded);

public slots:
void setLoaded(bool loaded);
};

#endif // BUSINESSLOGIC_H
