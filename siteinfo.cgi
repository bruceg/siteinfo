#!/bin/sh
exec 2>&1
echo "Content-Type: text/html"
echo
exec python -c 'import siteinfo; siteinfo.main()'
