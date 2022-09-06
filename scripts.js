// Open all external links in new tabs or windows
document.querySelectorAll('a[href^="http"]').forEach(link => link.target = '_blank');

if (window.tocbot) {
    tocbot.init({
        scrollSmooth: false,
        tocSelector: '.js-toc',
        contentSelector: '.main-content',
        disableTocScrollSync: true,
        headingSelector: 'h2'
    });
}