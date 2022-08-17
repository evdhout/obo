class OboException(Exception):
    """Base OBO Exception"""

    def __init__(self, message: str = 'OBOException'):
        self.message = message
        super(OboException, self).__init__(self.message)


class PersonWithoutBSNandOWN(OboException):
    """Trying to make a person without BSN and OWN"""

    def __init__(self):
        super(PersonWithoutBSNandOWN, self).__init__("Trying to create a person without BSN or OWN")


class DuplicatePerson(OboException):
    """Trying to add a person with an already existing Id"""

    def __init__(self, person_id: str):
        self.person_id = person_id
        super(DuplicatePerson, self).__init__(f"Duplicate person with id {person_id}")


class OboFileException(OboException):
    """Base OBO File Exception"""

    def __init__(self, line: str or None, line_number: int or None = None, message: str = 'OBOFileException'):
        self.line = line
        self.line_number = line_number
        super(OboFileException, self).__init__(message=f"{message}\n{line_number}:{line}")


class OboFileOpenError(OboFileException):
    """Raised when opening the OBO file fails"""

    def __init__(self, filename: str):
        self.filename = filename
        super(OboFileOpenError, self).__init__(message=f"Error opening OBO file {filename}")


class UnknownOboRecordType(OboFileException):
    """Raised when the OBO recordtype in the line is unknown"""

    def __init__(self, recordtype: str, line: str, line_number: int or None = None):
        self.recordtype = recordtype
        super(UnknownOboRecordType, self).__init__(line=line,
                                                   line_number=line_number,
                                                   message=f"Unknown OBO recordtype '{self.recordtype}'")


class UnexpectedOboRecordType(OboFileException):
    """Raised when teh OBO recordtype does not match the expected recordtype"""

    def __init__(self, recordtype: str, expected: str, line: str, line_number: int or None = None):
        message = f"Unexpected recordtype {recordtype}. Expecting recordtype {expected}"
        super(UnexpectedOboRecordType, self).__init__(line=line,
                                                      line_number=line_number,
                                                      message=message
                                                      )


class InvalidDateFormat(OboFileException):
    """Raised when teh OBO date text does not parse properly"""

    def __init__(self, date_string: str, line: str, line_number: int or None = None):
        self.date_string = date_string
        super(InvalidDateFormat, self).__init__(line=line,
                                                line_number=line_number,
                                                message=f"Invalid date {date_string}"
                                                )


class InvalidBooleanFormat(OboFileException):
    """Raised when the OBO boolean text does not parse properly"""

    def __init__(self, bool_string: str, line: str, line_number: int or None = None):
        self.bool_string = bool_string
        super(InvalidBooleanFormat, self).__init__(line=line,
                                                   line_number=line_number,
                                                   message=f"Invalid boolean {bool_string}"
                                                   )


class InvalidNumberFormat(OboFileException):
    """Raised when the OBO number text does not parse properly"""

    def __init__(self, number_string: str, line: str, line_number: int or None = None):
        self.number_string = number_string
        super(InvalidNumberFormat, self).__init__(line=line,
                                                  line_number=line_number,
                                                  message=f"Invalid number {number_string}"
                                                  )


class InvalidOboRecordFormat(OboFileException):
    """Raised when the line in the OBO is not formatted correctly"""

    def __init__(self, line: str, line_number: int or None = None):
        super(InvalidOboRecordFormat, self).__init__(line=line,
                                                     line_number=line_number,
                                                     message="Problem in OBO line format")


class OboRecordWithoutBSNandOWN(OboFileException):
    """Raised when the person has no BSN and no OWN"""

    def __init__(self, line: str, line_number: int or None = None):
        super(OboRecordWithoutBSNandOWN, self).__init__(line=line,
                                                        line_number=line_number,
                                                        message="Obo Record has no BSN and no OWN")
