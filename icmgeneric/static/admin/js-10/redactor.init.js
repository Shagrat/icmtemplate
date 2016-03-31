$(function()
{
    $('.redactor').redactor({
        minHeight: 250,
        maxHeight: 500,
        plugins: [
            'fontcolor',
            'fontsize',
            'imagemanager',
            'video',
            'table',
            'fullscreen'
        ],
        imageUpload: '/ajax/fileupload/',
        imageManagerJson: '/ajax/imagelist/',
        buttonSource: true,
        convertDivs: false,
        replaceDivs: false,
        paragraphize: false,
        removeWithoutAttr: false,
		removeEmpty: false,
        formattingAdd: [
        {
            tag: 'span',
            title: 'Underline',
            style: 'text-decoration:underline;'
        }]

    });
});
