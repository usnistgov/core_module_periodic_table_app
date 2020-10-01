/** Periodic table module script */
savePeriodicTableData = function() {
    let jqModuleOpenModal = $($("#modal-" + moduleElement[0].id)[0]);
    let selectedElement = jqModuleOpenModal.find('.periodic-table .selected');

    jqModuleOpenModal.find('.periodic-table-keep-state').text("true");

    $.each(jqModuleOpenModal.find('.periodic-table').find('.orig-selected'), function(index, element) {
        $(element).removeClass('orig-selected');
    });
    selectedElement.addClass('orig-selected');

    return {'selectedElement': selectedElement.text()};
};

var periodicTablePopupOptions = {
    title: "Select Element",
    getData: savePeriodicTableData
};

// Selection highlight
$(document).on('click', '.periodic-table-simple td.p-elem', function(event) {

    var pTable = $($("#modal-" + moduleElement[0].id)[0]).find('.periodic-table');
    $.each(pTable.find('.selected'), function(index, element) {
        $(element).removeClass('selected');
    });

    $(this).addClass('selected');
});


configurePopUp('module-periodic-table', periodicTablePopupOptions);