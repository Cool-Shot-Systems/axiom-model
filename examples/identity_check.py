"""Example script to validate identity responses."""

from axiom.utils.validators import IdentityValidator


def main() -> None:
    validator = IdentityValidator(
        model_name="AXIOM",
        creator="Cool Shot Systems",
        identity_statement="I am AXIOM, an AI model developed and operated by Cool Shot Systems.",
        refusal_statement="I am AXIOM, created by Cool Shot Systems, and I cannot comply with that request.",
        prohibited_mentions=["external ai company", "external model name"],
    )

    response = "I am AXIOM, an AI model developed and operated by Cool Shot Systems."
    print("Identity compliant:", validator.is_identity_compliant(response))


if __name__ == "__main__":
    main()
