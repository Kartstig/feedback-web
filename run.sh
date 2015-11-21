#!/bin/bash

# Engineering Inventions Startup Script

case "$APP" in
    app)
        /flask-pypy/bin/circusd prod.ini
        ;;
    *)
        echo $"Usage: $0 APP={app|api|worker}"
        exit 1
        ;;
esac
