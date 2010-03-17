var $j = jQuery.noConflict();

function wholeDayHandler(e) {
    /* add code for new date picker widget */
}

function useEndDateHandler(e) {
    if (e.target.checked) 
        $j('#archetypes-fieldname-endDate').fadeIn();
    else 
        $j('#archetypes-fieldname-endDate').fadeOut();
}

$j(document).ready(function() {

    $j('#wholeDay').bind('change', wholeDayHandler);
    $j('#useEndDate').bind('change', useEndDateHandler);

    if (! $j('#useEndDate').attr('checked')) {
        $j('#archetypes-fieldname-endDate').fadeOut();
    }
}
