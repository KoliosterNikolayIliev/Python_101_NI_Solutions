def reduce_file_path(path):
    path = path.split('/')
    result = []
    
    for index in range(len(path)):
        if path[index] == '..':
            path[index - 1] = ''
            path[index] = ''
        if path[index] == '.':
            path[index] = ''
    for symbol in path:
        if symbol != '':
            result.append(symbol)
    result = '/' + '/'.join(result)

    return result



tests = [
    reduce_file_path("/") == "/",
    reduce_file_path("/srv/../") == "/",
    reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf",
    reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf",
    reduce_file_path("/srv/./././././") == "/srv",
    reduce_file_path("/etc//wtf/") == "/etc/wtf",
    reduce_file_path("/etc/../etc/../etc/../") == "/",
    reduce_file_path("//////////////") == "/",
    reduce_file_path("/../") == "/",
]

[print(x) for x in tests]
