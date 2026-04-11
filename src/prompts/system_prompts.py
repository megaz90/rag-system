from src.core.config import COMPANY

# Mainly used for LLM at pipeline final stage to generate final answer
MAIN_SYSTEM_PROMPT = f"""
{COMPANY} is a comprehensive business management platform.

It provides tools for:
- sales and purchase management
- accounting and cash management
- inventory tracking
- customer and supplier management
- employee and user access management
- reporting and business insights

The platform includes detailed documentation and manuals that explain features, workflows, and system configuration.

Users typically ask questions to:
- understand how to use features
- navigate the system
- configure settings
- troubleshoot workflows
"""

# A small software domain prompt which helps the LLM understand the context.
DOMAIN_HINT = f"""
The system contains documentation for {COMPANY}, a business management platform
covering accounting, inventory, sales, HR, and workflows.
"""

# Default Prompt for LLM
DEFAULT_SYSTEM_PROMPT = """You are a helpful assistant that answers questions based on the provided context."""
