#!/bin/bash

# Script para vm Kali preinstaladas
# cambiar nombre usuario desde cuenta root tras reiniciar
# EJECUTAR DESDE CONSOLA

name="artp3r"

echo usermod -l $name -d /home/$name -m kali
usermod -l $name -d /home/$name -m kali
sleep 3
echo groupmod -n $name kali
groupmod -n $name kali
sleep 3
echo chfn -f $name $name
chfn -f $name $name
sleep 3
echo dpkg-reconfigure keyboard-configuration
dpkg-reconfigure keyboard-configuration
sleep 3
# Otros cambios:
# Nombre máquina en /etc/hosts y /etc/hostname
# systemctl set-default multi-user.target # para máquinas con pocos recursos

sudo echo "set bell-style none" >> /etc/inputrc # elimina el beep (water drop)
# o bien editar el fichero y descomentar esa linea


# VMWARE: cambiar kali por artp3r en:
# /home/${newUserName}/.cache/sessions/xfce4-session-${computerName}:0

# Contraseña al final
