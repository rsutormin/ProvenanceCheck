/*
A KBase module: ProvenanceCheck
*/

module ProvenanceCheck {
    funcdef get_service_props() returns (mapping<string,string>) authentication optional;
    funcdef hello_string(string name) returns (string) authentication optional;
};
