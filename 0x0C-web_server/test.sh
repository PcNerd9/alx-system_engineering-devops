#!/usr/bin/env bash

new_test="Make sure to adjust the multiline_text and file_path
and line_number variable according
to your specific use case. Also, not that the -i option
in sed will modify the file in place
so use it with caution
the text to replace
"
line_to_replace="the text to replace"
file_path=some_page.html
escaped_lines=$(echo "$new_test" | sed ':a;N;$!ba;s/\n/\\n/g;s/[\/&]/\\&/g')

sed "s/$line_to_replace/$escaped_lines/g" $file_path
