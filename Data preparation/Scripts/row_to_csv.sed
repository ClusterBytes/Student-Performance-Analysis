/[A-Z]\{3\}[0-9]\{2\}[A-Z]\{2\}[0-9]\{3\}.*/,$s/\([A-Z]\{3\}[0-9]\{2\}[A-Z]\{2\}[0-9]\{3\}\).*Attendance:\(.*\)Internals:\([0-9]*\.[0-9]*\/[0-9]*\).*/\1,\2,\3/g