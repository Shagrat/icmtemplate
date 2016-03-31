if (typeof RedactorPlugins === 'undefined') var RedactorPlugins = {};

RedactorPlugins.filebrowser = {
    init: function()
    {
        this.buttonAdd('filebrowser', 'File Browser', this.showMyModal);
    },
    showMyModal: function()
    {
        var callback = $.proxy(function()
        {
            this.selectionSave();
            $('#redactor_modal #filebrowser-insert').click($.proxy(this.insertFromMyModal, this));

        }, this);

        var filebrowserCallback = $.proxy(function(data){
            this.modalInit('File Browser', data, 500, callback);
            $( "#selectable" ).selectable();
//            console.log($( "#selectable" ))
        }, this)
        // modal call
        $.get( "/ajax/filebrowser/", filebrowserCallback);

    },
    insertFromMyModal: function(html)
    {
        this.selectionRestore();
        this.insertHtml($('#filebrowser-textarea').val());
        this.modalClose();
    }
}