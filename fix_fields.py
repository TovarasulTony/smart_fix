import datetime



class Fix:
    def __init__(self):
        self.seqNo = 0

    def field_8_begin_string(self):
        return "8=FIX4.4|"

    def field_9_body_length(self):
        return "9=???????????????????????????|"

    def field_10_check_sum(self):
        return "9=???????????????????????????|"

    def field_34_msg_seq_num(self):
        self.seqNo += 1
        return "34=" + str(self.seqNo) + "|"

    def field_35_msg_type(self):
        return "35=A|"

    def field_49_sender_comp_id(self):
        return "49=LME|"

    def field_52_sending_time(self):
        ret = "52="
        var = datetime.datetime.now()
        var = str(var)
        ret += var[:4] + var[5:7] + var[8:10] + '-' + var[11:]
        ret += "|"
        return ret

    def field_56_target_comp_id(self):
        return "56=SNCFIXRTGENA|"

    def field_98_encrypt_method(self):
        return "98=0|"

    def field_108_heart_bt_int(self):
        return "108=30|"

    def field_141_reset_seq_num_flag(self):
        return "141=Y|"

    def field_9_body_length(self):
        return "9=???????????????????????????|"

    def field_9_body_length(self):
        return "9=???????????????????????????|"
