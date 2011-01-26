#!/bin/sh
exec 2>&1
echo "Content-Type: text/html"
echo
exec /usr/bin/python -c 'import siteinfo; siteinfo.main()'
