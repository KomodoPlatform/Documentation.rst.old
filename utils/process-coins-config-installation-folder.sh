#!/bin/bash
for filename in ~/gitrepos/Documentation/coin-configs-install-instructions/*; do
    filename=${filename//\/home\/gcharang\/gitrepos\/Documentation\/coin\-configs\-install\-instructions\/}
    echo "$filename" >> output.rst
    if [ ${#filename} = 2 ]; then
      echo "==" >> output.rst
    elif [ ${#filename} = 3 ]; then
      echo "===" >> output.rst
    elif [ ${#filename} = 4 ]; then
      echo "====" >> output.rst
    elif [ ${#filename} = 5 ]; then
      echo "=====" >> output.rst
    elif [ ${#filename} = 6 ]; then
      echo "======" >> output.rst
    elif [ ${#filename} = 7 ]; then
      echo "=======" >> output.rst
    elif [ ${#filename} = 8 ]; then
      echo "========" >> output.rst
    elif [ ${#filename} = 9 ]; then
      echo "=========" >> output.rst
    fi
    echo "" >> output.rst
    echo ".. include:: coin-configs-install-instructions/$filename" >> output.rst
    echo "   :literal:" >> output.rst
    echo "" >> output.rst
done
