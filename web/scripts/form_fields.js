var form_fields = {
    name: '',
    type: '',
    qualities: {
        grapes: [],
        year: ''
    },
    awards: [],
    rating: {
        min: '',
        max: ''
    },
    geography: {
        country: '',
        region: '',
        vineyard: ''
    },
    purchase: {
        price: '',
        date: '',
        location: ''
    },
    targets: {
        drinkby: '',
        drinkfor: ''
    },
    pairings: []
};

$('#add-grape').click(function () {
    form_fields.qualities.grapes.push($('#grape-type').val());
    $('#new-grape').before('');
});