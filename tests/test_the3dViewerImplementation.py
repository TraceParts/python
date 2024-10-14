from unittest import TestCase

from src.the3dViewerImplementation import the_3d_viewer_implementation


class Test(TestCase):
    def test_the_3d_viewer_implementation(self):
        # values from https://developers.traceparts.com/v2/reference/3d-viewer-implementation#example-of-3d-viewer-call
        response = the_3d_viewer_implementation(elsid="phoenix-contact",
                                                culture_info="en",
                                                optional_parameters={
                                                    "SupplierID": "PHOENIX_CONTACT",
                                                    "PartNumber": "1857837",
                                                })
        print(response)
        expected_url = "https://www.traceparts.com/els/phoenix-contact/en/api/viewer/3d?&SupplierID=PHOENIX_CONTACT&PartNumber=1857837"
        self.assertEqual(expected_url, response)

    def test_the_3d_viewer_implementation_with_spinning(self):
        # values from https://developers.traceparts.com/v2/reference/3d-viewer-implementation#example-of-3d-viewer-call
        response = the_3d_viewer_implementation(elsid="phoenix-contact",
                                                culture_info="en",
                                                optional_parameters={
                                                    "SupplierID": "PHOENIX_CONTACT",
                                                    "PartNumber": "1857837",
                                                    "EnablePresentationMode": "true"  # added value for testing
                                                })
        print(response)
        expected_url = "https://www.traceparts.com/els/phoenix-contact/en/api/viewer/3d?&SupplierID=PHOENIX_CONTACT&PartNumber=1857837&EnablePresentationMode=true"
        self.assertEqual(expected_url, response)
