#!/bin/bash
echo "Content-Type: text/html"
echo
exec python -c 'import siteinfo; siteinfo.main()' 2>&1
