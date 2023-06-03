import datetime



class Fix:
    def __init__(self):
        self.seqNo = 0

    def make_login(self):
        login_string = ""
        login_string += self.field_35_msg_type()
        login_string += self.field_34_msg_seq_num()
        login_string += self.field_49_sender_comp_id()
        login_string += self.field_52_sending_time()
        login_string += self.field_56_target_comp_id()
        login_string += self.field_98_encrypt_method()
        login_string += self.field_108_heart_bt_int()
        login_string += self.field_141_reset_seq_num_flag()
        login_string = self.field_9_body_length(login_string) + login_string
        login_string = self.field_8_begin_string() + login_string

        login_string += self.field_10_check_sum(login_string)

    def field_8_begin_string(self):
        return "8=FIX4.4|"

    def field_9_body_length(self, msg):
        return "9=" + size(msg) + "|"

    def field_10_check_sum(self, msg):
        cks = 0
    
        for x in msg:
            cks += ord(x)
        cks %= 256

        sprintf( tmpBuf, "%03d", (unsigned int)( cks % 256 ) );
        return( tmpBuf );
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
