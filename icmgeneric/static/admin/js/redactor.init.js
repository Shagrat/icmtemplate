	$(function()
	{
		$('.redactor').redactor({
            minHeight: 250,
            maxHeight: 500,
            plugins: ['fontcolor','fontsize' ],
            imageUpload: '/ajax/fileupload/',
            imageGetJson: '/ajax/imagelist/',
            convertDivs: false,
            replaceDivs: false,
            paragraphize: false,
            removeWithoutAttr: false,
		    removeEmpty: false
		});
	});
