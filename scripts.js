// Open all external links in new tabs or windows
document.querySelectorAll('a[href^="http"]').forEach(link => link.target = '_blank');