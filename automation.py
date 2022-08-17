#  Sample database
auto_names = ['Auto', 'Auto1', 'Auto2']

triggers = ['1. Opt-in', '2. Time trigger', '3. Campaign activity', '4. Removed from list',
            '5. Purchase activity', '6. list trigger', '7. Page visited', '8. Registered or attended webinar']

actions = ['1. Send Email', '2. Add delay', '3. add to list', '4. Journey ejection',
           '5. Apply or remove tags', '6. Webinar registration']

conditions = [
    '1. Campaign status', '2. On list segment', '3. Has visited page',
    '4. Checklist field', '5. Check purchase status', '6. Webinar status']

automations_list = []


# Creating a new automation
def new_automation():
    choice = input('Given Options below;\n'
                   'A - Autoresponder. \nE - Ecommerce & marketing. \nB - Blank.'
                   '\n ==> Type the letter corresponding to the automation you want: ').lower()
    choices = ['a', 'e', 'b']
    print('')
    if choice.isalpha() and choice in choices:
        if choice == 'a':
            print('Autoresponder automation selected.')
            auto = Autoresponder(unique_name())
            automations_list.append(auto)
            print('')
            auto_choice = str(input('Enter number; '
                                    '\n1. Subscriber welcome emails'
                                    '\n2. Response to subscriber changes'
                                    '\n: '))
            if auto_choice == '1':
                print('')
                return auto.welcome_msg()
            elif auto_choice == '2':
                print('')
                return auto.response_msg()

        elif choice == 'e':
            print('Ecommerce & Marketing automation selected.')
            auto = EcommerceMarketing(unique_name())
            automations_list.append(auto)
            print('')
            auto_choice = str(input('Enter number; '
                                    '\n1. Thanking first-time customers'
                                    '\n2. Enable order notifications'
                                    '\n3. Abandoned cart email'
                                    '\n4. Retarget site visitors'
                                    '\n: '))
            if auto_choice == '1':
                print('')
                return auto.thanking_msg()
            elif auto_choice == '2':
                print('')
                return auto.enable_order_msg()
            elif auto_choice == '3':
                print('')
                return auto.abandoned_cart_msg()
            elif auto_choice == '4':
                print('')
                return auto.retarget_site_visitors()

        elif choice == 'b':
            print('Follow prompts to create custom automation.')
            auto = Blank(unique_name())
            automations_list.append(auto)
            print('')
            content()
            print('')
            custom_journey()

            return auto.success_msg()

        dashboard()

    else:
        print('Invalid input.')


# Automation types
class Autoresponder:
    def __init__(self, name):
        self.name = name

    def welcome_msg(self):
        print('Emails to introduce yourself will be sent to New subscribers')

    def response_msg(self):
        print('Email will be sent when a subscriber joins a list segment')


class EcommerceMarketing:
    def __init__(self, name):
        self.name = name

    def thanking_msg(self):
        print('Thank first time customers')

    def enable_order_msg(self):
        print('Beautify receipts and shipping updates')

    def abandoned_cart_msg(self):
        print('Email as a Friendly reminder who leave the store without checking out.')

    def retarget_site_visitors(self):
        print('Email to Remind people of cool stuff they saw on your website')


class Blank:
    def __init__(self, name):
        self.name = name

    def success_msg(self):
        print('Automation started successfully')


# Triggers
def opt_in():
    print('==> Subscriptions monitored in selected list ')


def time_trigger(list_item, date, time, timezone, current_time):
    pass


def campaign_activity(list_item, email, activity):
    pass


def removed_from_list(list_item):
    pass


def purchase_activity(list_item, status, purchase, store, product):
    pass


def list_trigger(list_item):
    pass


def page_visited(list_item, page, status):
    pass


def registered_webinar(list_item, webinar, status):
    pass


trigger_elements = {
    1: opt_in, 2: time_trigger, 3: campaign_activity,
    4: removed_from_list, 5: purchase_activity, 6: list_trigger, 7: page_visited, 8: registered_webinar
}


# Action elements
def send_email():
    print('==> Email sent to subscribers filtered from an upstream trigger element')
    pass


def add_delay():
    pass


def add_remove_list():
    pass


def journey_ejection():
    pass


def apply_remove_tags():
    pass


def webinar_reg():
    pass


action_elements = {
    1: send_email, 2: add_delay, 3: add_remove_list,
    4: journey_ejection, 5: apply_remove_tags, 6: webinar_reg
}


# Condition elements
def campaign_status():
    print('==> Checks campaign status and pass the subscribers that meet the conditions to a downstream journey')
    pass


def on_list_segment():
    pass


def has_visited_page():
    pass


def checklist_field():
    pass


def check_purchase_status():
    pass


def webinar_status():
    pass


condition_elements = {
    1: campaign_status, 2: on_list_segment, 3: has_visited_page,
    4: checklist_field, 5: check_purchase_status, 6: webinar_status
}


# Dashboard

Auto = Autoresponder('Auto')
Auto1 = EcommerceMarketing('Auto1')
Auto2 = Blank('Auto2')
automations_list.append(Auto)
automations_list.append(Auto1)
automations_list.append(Auto2)


def dashboard():
    print('')
    print(f'AUTOMATIONS - {len(automations_list)}')
    for automation in automations_list:
        print(f'{automation.name} is running')
        print(f'    Published:    {"pub_date"}')
        print(f'    Last_edited:  {"edit_date"}')
        print('')

    pass


# Helper functions
def unique_name():
    name = str(input('==> Enter a name for this automation: '))
    while name in auto_names or name == '' or name.isspace():
        if name == '' or name.isspace():
            print('')
            name = str(input('==> Please enter a name for this automation: '))
        else:
            print('You already have an automation with this name')
            print('')
            name = str(input('==> Enter a different name for this automation: '))

    auto_names.append(name)
    return name


def index_exists(list_item, index):
    if 0 <= index < len(list_item):
        return True
    else:
        return False


def content():
    print(f'{"TRIGGERS":<45} {"ACTIONS":<45} {"CONDITIONS":<40}')
    print(f'{"-" * 40:<45} {"-" * 40:<45} {"-" * 40:<40}')
    for index in range(len(triggers)):
        if index_exists(triggers, index) and index_exists(actions, index) and index_exists(conditions, index):
            print(f'{triggers[index]:<45} {actions[index]:<45} {conditions[index]:<40}')
        elif not index_exists(actions, index) and not index_exists(conditions, index):
            print(f'{triggers[index]:<45} {" ":<45} {" ":<40}')
    print(f'{"-" * 40:<45} {"-" * 40:<45} {"-" * 40:<40}')
    print('From the above menu you are to choose the elements to add to your journey;'
          '\n==> Triggers start journeys'
          '\n==> Actions do things'
          '\n==> Conditions check things')


def custom_journey():
    journey_trigger = int(input('Enter trigger: '))
    journey_action = int(input('Enter action: '))
    journey_condition = int(input('Enter condition: '))
    print('')
    trigger_elements[journey_trigger]()
    action_elements[journey_action]()
    condition_elements[journey_condition]()
