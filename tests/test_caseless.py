from unittest import TestCase, main

from incase import Case, Caseless

test_string = "test string"

expected = {
    "CASELESS": Caseless("test string"),
    "CAMEL": "testString",
    "DROMEDARY": "testString",
    "MEDIAL": "testString",
    "SNAKE": "test_string",
    "PASCAL": "TestString",
    "INITIAL_CAPITALS": "TestString",
    "KEBAB": "test-string",
    "DASH": "test-string",
    "UPPER_SNAKE": "TEST_STRING",
    "UPPERCASE": "TEST STRING",
    "UPPER": "TEST STRING",
    "LOWERCASE": "test string",
    "LOWER": "test string",
    "TITLE": "Test String",
    "ALTERNATING": "TeSt sTrIng",
    "SARCASM": "TeSt sTrIng",
    "ORIGINAL": "test string",
    "WORD": "test string",
    Case.CASELESS: Caseless("test string"),
    Case.CAMEL: "testString",
    Case.DROMEDARY: "testString",
    Case.MEDIAL: "testString",
    Case.SNAKE: "test_string",
    Case.PASCAL: "TestString",
    Case.INITIAL_CAPITALS: "TestString",
    Case.KEBAB: "test-string",
    Case.DASH: "test-string",
    Case.UPPER_SNAKE: "TEST_STRING",
    Case.UPPERCASE: "TEST STRING",
    Case.UPPER: "TEST STRING",
    Case.LOWERCASE: "test string",
    Case.LOWER: "test string",
    Case.TITLE: "Test String",
    Case.ALTERNATING: "TeSt sTrIng",
    Case.SARCASM: "TeSt sTrIng",
    Case.ORIGINAL: "test string",
    Case.WORD: "test string",
}


class TestCaseless(TestCase):
    def test_cases(self):
        for case, value in expected.items():
            with self.subTest(msg=f"test {case}", case=case, value=value):
                self.assertEqual(Caseless(test_string)[case], value)


if __name__ == "__main__":
    main()
