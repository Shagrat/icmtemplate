$(function()
{
    var redactorOpts = {
        replaceDivs:false,
        plugins: [
            'fontcolor',
            'fontsize',
            'imagemanager',
            'icminline',
            'table',
            'fullscreen'
        ],
        imageUpload: '/ajax/fileupload/',
        imageManagerJson: '/ajax/imagelist/',
        buttonSource: true,
        convertDivs: false,
        paragraphize: false,
        removeWithoutAttr: false,
		removeEmpty: false,
        formattingAdd: [
        {
            tag: 'span',
            title: 'Underline',
            style: 'text-decoration:underline;'
        }]

    };
    $('.redactor').dblclick(function(){
        if ($(this).parent().hasClass('redactor-box')){
            return false;
        }
        $(this).redactor(redactorOpts);
    });
});
