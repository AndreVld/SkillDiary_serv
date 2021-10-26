$('document').ready(function () {
    let note = $('#note')[0];
    let url = $('#url')[0];
    let file = $('#file')[0];

    function hide_all() {
        [note, url, file].forEach(el => el.classList.add('d-none'));
    }

    $('select[name="type_info"]').change(function () {
        switch (this.value) {
            case 'TEXT':
                hide_all();
                note.classList.remove('d-none');
                break;
            case 'URL':
                hide_all();
                url.classList.remove('d-none');
                break;
            case 'FILE':
                hide_all();
                file.classList.remove('d-none');
                break;
        }
    });
});