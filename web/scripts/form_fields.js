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

Array.prototype.remove = function() {
    var what, a = arguments, L = a.length, ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};

$(function (){

    $('#test').click(function() {
        console.log('clickekekeke');
    });

    $('#add-grape').click(function () {
        if($('#grape-type').val() === '' || form_fields.qualities.grapes.includes($('#grape-type').val())) return;
        form_fields.qualities.grapes.push($('#grape-type').val());        
        $('#new-grape').before('<div class="flex-row"><h3>' + $('#grape-type').val() + '</h3><div class="padding-width"><input type="reset" id="grape" content="' + $('#grape-type').val() + '"></div></div>');
        $('#grape-type').val('');
        updateButtons();
    });

    $('#add-award').click(function () {
        if($('#award-type').val() === '' || form_fields.awards.includes($('#award-type').val())) return;
        form_fields.awards.push($('#award-type').val());        
        $('#new-award').before('<div class="flex-row"><h3>' + $('#award-type').val() + '</h3><div class="padding-width"><input type="reset" id="award" content="' + $('#award-type').val() + '"></div></div>');
        $('#award-type').val('');
        updateButtons();
    });

    $('#add-pairing').click(function () {
        if($('#painring-type').val() === '' || form_fields.pairings.includes($('#pairing-type').val())) return;
        form_fields.pairings.push($('#pairing-type').val());        
        $('#new-pairing').before('<div class="flex-row"><h3>' + $('#pairing-type').val() + '</h3><div class="padding-width"><input type="reset" id="pairing" content="' + $('#pairing-type').val() + '"></div></div>');
        $('#pairing-type').val('');
        updateButtons();
    });
    
    updateButtons();
});

function updateButtons() {
    $(':button, input[type="reset"]').click(function(){
        if (this.id === 'grape') {
            form_fields.qualities.grapes.remove($(this).attr('content'));
        } else if (this.id === 'award') {
            form_fields.awards.remove($(this).attr('content'));
        } else if (this.id === 'pairing') {
            form_fields.pairings.remove($(this).attr('content'));
        }
        $(this).parent().parent().remove();
        console.log(form_fields.awards);
    });
}