# BlueButtonDev
This is the Developer Registration Application for the Medicare BlueButton data API. This application handles Developer Registration, Entity Validation and the management of OAuth Application keys.

This is one part of a three part application suite:

0.  BlueButtonUser - Front-end user application 
    ( https://github.com/ekivemark/BlueButtonUser )
0.  BlueButtonDev - Front-end Developer administration application
    ( https://github.com/ekivemark/BlueButtonDev )
0.  BlueButtonFHIR_API - Public API providing authenticated pass-through to back-end FHIR Services. 
    ( https://github.com/ekivemark/BlueButtonFHIR_API ) 
 
Changelist:

*   Basic account registration with username for Third Party Application Developers.
*   Developers will need to pass third party Whitelist Trust Verification before 
    being allowed to create or manage application keys.

Latest Change:

*   Fixed test call to Trust whitelist in appmgmt.views.trust.py
