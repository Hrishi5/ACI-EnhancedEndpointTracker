import {Component, OnInit} from '@angular/core';
import {PreferencesService} from "../../../_service/preferences.service";
import {environment} from '../../../../environments/environment.standalone';

@Component({
    selector: 'app-connectivity',
    templateUrl: './connectivity.component.html',
})

export class ConnectivityComponent implements OnInit {
    inputs = [];
    app_mode = environment.app_mode;

    constructor(public prefs: PreferencesService) {
        this.inputs = [
            {name: 'Hostname', model: 'apic_hostname', type: 'text', hidden: ''},
            {name: 'APIC Certificate', model: 'apic_cert', type: 'text', hidden: 'app_mode'},
            {name: 'Username', model: 'apic_username', type: 'text', hidden: ''},
            {name: 'Password', model: 'apic_password', type: 'password', hidden: ''},
            {name: 'SSH Username', model: 'ssh_username', type: 'text', hidden: ''},
            {name: 'SSH Password', model: 'ssh_password', type: 'password', hidden: ''}
        ]
    }

    ngOnInit() {
    }

}
