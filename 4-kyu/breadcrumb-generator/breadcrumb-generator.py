        return '<span class="active">HOME</span>'
​
    
    path_parts[-1] = re.sub(r'\.(html?|php|asp)$', '', path_parts[-1], flags=re.I)
​
    breadcrumb = ['<a href="/">HOME</a>']
​
    for i, part in enumerate(path_parts):
        display = part.replace('_', '-')
        if len(display) > 30:
            words = [w for w in display.split('-') if w not in ignore]
            display = ''.join(w[0] for w in words)
        else:
            display = display.replace('-', ' ')
        display = display.upper()
​
        if i == len(path_parts) - 1:
            breadcrumb.append(f'<span class="active">{display}</span>')
        else:
            href = '/' + '/'.join(path_parts[:i+1]) + '/'
            breadcrumb.append(f'<a href="{href}">{display}</a>')
​
    return separator.join(breadcrumb)
​