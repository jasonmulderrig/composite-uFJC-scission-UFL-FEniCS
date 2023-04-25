"""The module for the composite uFJC single chain scission model
implemented in the Unified Form Language (UFL) for FEniCS.
"""

# Import external modules
from __future__ import division
from dolfin import *
from composite_ufjc_scission import (
    RateIndependentScissionCompositeuFJC,
    RateDependentScissionCompositeuFJC,
    RateIndependentSmoothstepScissionCompositeuFJC,
    RateDependentSmoothstepScissionCompositeuFJC,
    RateIndependentSigmoidScissionCompositeuFJC,
    RateDependentSigmoidScissionCompositeuFJC
)

# Import internal modules
from .rate_dependence_scission import (
    RateIndependentScissionUFLFEniCS,
    RateDependentScissionUFLFEniCS
)
from .scission_model import (
    AnalyticalScissionCompositeuFJCUFLFEniCS,
    SmoothstepScissionCompositeuFJCUFLFEniCS,
    SigmoidScissionCompositeuFJCUFLFEniCS
)


class RateIndependentScissionCompositeuFJCUFLFEniCS(
        RateIndependentScissionUFLFEniCS,
        AnalyticalScissionCompositeuFJCUFLFEniCS):
    """The composite uFJC single-chain model class with rate-independent
    stochastic scission implemented in the Unified Form Language (UFL)
    for FEniCS.
    
    This class is a representation of the composite uFJC single-chain
    model with rate-independent stochastic scission implemented in the
    Unified Form Language (UFL) for FEniCS; an instance of this class is
    a composite uFJC single-chain model instance with rate-independent
    stochastic scission implemented in the Unified Form Language (UFL)
    for FEniCS. It inherits all attributes and methods from the
    ``RateIndependentScissionUFLFEniCS`` class. It also inherits all
    attributes and methods from the
    ``AnalyticalScissionCompositeuFJCUFLFEniCS`` class, which inherits
    all attributes and methods from the ``CompositeuFJCUFLFEniCS``
    class.
    """
    def __init__(self, **kwargs):
        """
        Initializes the
        ``RateIndependentScissionCompositeuFJCUFLFEniCS`` class,
        producing a composite uFJC single-chain model instance with
        rate-independent stochastic scission implemented in the Unified
        Form Language (UFL) for FEniCS.
        
        Initialize and inherit all attributes and methods from the
        ``RateIndependentScissionUFLFEniCS`` class instance and the
        ``AnalyticalScissionCompositeuFJCUFLFEniCS`` class instance.
        """
        composite_ufjc = RateIndependentScissionCompositeuFJC(**kwargs)

        # Core composite uFJC single-chain model constants
        self.cond_val = Constant(composite_ufjc.cond_val)
        
        self.nu = Constant(composite_ufjc.nu)
        self.zeta_nu_char = Constant(composite_ufjc.zeta_nu_char)
        self.kappa_nu = Constant(composite_ufjc.kappa_nu)
        
        self.lmbda_nu_ref = Constant(composite_ufjc.lmbda_nu_ref)
        self.lmbda_c_eq_ref = Constant(composite_ufjc.lmbda_c_eq_ref)
        self.lmbda_nu_crit = Constant(composite_ufjc.lmbda_nu_crit)
        self.lmbda_c_eq_crit = Constant(composite_ufjc.lmbda_c_eq_crit)
        self.xi_c_crit = Constant(composite_ufjc.xi_c_crit)
        
        self.lmbda_c_eq_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_c_eq_pade2berg_crit)
        )
        self.lmbda_nu_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_nu_pade2berg_crit)
        )

        # Analytical scission model constants
        self.epsilon_nu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_nu_diss_hat_crit)
        )
        self.epsilon_cnu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_cnu_diss_hat_crit)
        )
        self.A_nu = Constant(composite_ufjc.A_nu)
        self.Lambda_nu_ref = Constant(composite_ufjc.Lambda_nu_ref)

        del composite_ufjc

        RateIndependentScissionUFLFEniCS.__init__(self)
        AnalyticalScissionCompositeuFJCUFLFEniCS.__init__(self)


class RateDependentScissionCompositeuFJCUFLFEniCS(
        RateDependentScissionUFLFEniCS,
        AnalyticalScissionCompositeuFJCUFLFEniCS):
    """The composite uFJC single-chain model class with rate-dependent
    stochastic scission implemented in the Unified Form Language (UFL)
    for FEniCS.
    
    This class is a representation of the composite uFJC single-chain
    model with rate-dependent stochastic scission implemented in the
    Unified Form Language (UFL) for FEniCS; an instance of this class is
    a composite uFJC single-chain model instance with rate-dependent
    stochastic scission implemented in the Unified Form Language (UFL)
    for FEniCS. It also inherits all attributes and methods from the
    ``RateDependentScissionUFLFEniCS`` class. It also inherits all
    attributes and methods from the
    ``AnalyticalScissionCompositeuFJCUFLFEniCS`` class, which inherits
    all attributes and methods from the ``CompositeuFJCUFLFEniCS``
    class.
    """
    def __init__(self, **kwargs):
        """
        Initializes the ``RateDependentScissionCompositeuFJCUFLFEniCS``
        class, producing a composite uFJC single-chain model instance
        with rate-dependent stochastic scission implemented in the
        Unified Form Language (UFL) for FEniCS.
        
        Initialize and inherit all attributes and methods from the
        ``RateDependentScissionUFLFEniCS`` class instance and the
        ``AnalyticalScissionCompositeuFJCUFLFEniCS`` class instance.
        """
        composite_ufjc = RateDependentScissionCompositeuFJC(**kwargs)

        # Core composite uFJC single-chain model constants
        self.cond_val = Constant(composite_ufjc.cond_val)
        
        self.nu = Constant(composite_ufjc.nu)
        self.zeta_nu_char = Constant(composite_ufjc.zeta_nu_char)
        self.kappa_nu = Constant(composite_ufjc.kappa_nu)
        
        self.lmbda_nu_ref = Constant(composite_ufjc.lmbda_nu_ref)
        self.lmbda_c_eq_ref = Constant(composite_ufjc.lmbda_c_eq_ref)
        self.lmbda_nu_crit = Constant(composite_ufjc.lmbda_nu_crit)
        self.lmbda_c_eq_crit = Constant(composite_ufjc.lmbda_c_eq_crit)
        self.xi_c_crit = Constant(composite_ufjc.xi_c_crit)
        
        self.lmbda_c_eq_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_c_eq_pade2berg_crit)
        )
        self.lmbda_nu_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_nu_pade2berg_crit)
        )

        # Analytical scission model constants
        self.epsilon_nu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_nu_diss_hat_crit)
        )
        self.epsilon_cnu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_cnu_diss_hat_crit)
        )
        self.A_nu = Constant(composite_ufjc.A_nu)
        self.Lambda_nu_ref = Constant(composite_ufjc.Lambda_nu_ref)

        # Rate dependent scission constant
        self.omega_0 = Constant(composite_ufjc.omega_0)

        del composite_ufjc

        RateDependentScissionUFLFEniCS.__init__(self)
        AnalyticalScissionCompositeuFJCUFLFEniCS.__init__(self)


class RateIndependentSmoothstepScissionCompositeuFJCUFLFEniCS(
        RateIndependentScissionUFLFEniCS,
        SmoothstepScissionCompositeuFJCUFLFEniCS):
    """The composite uFJC single-chain model class with rate-independent
    stochastic scission enforced via smoothstep scission implemented in
    the Unified Form Language (UFL) for FEniCS.
    
    This class is a representation of the composite uFJC single-chain
    model with rate-independent stochastic scission enforced via
    smoothstep scission implemented in the Unified Form Language (UFL)
    for FEniCS; an instance of this class is a composite uFJC
    single-chain model instance with rate-independent stochastic
    scission enforced via smoothstep scission implemented in the Unified
    Form Language (UFL) for FEniCS. It inherits all attributes and
    methods from the ``RateIndependentScissionUFLFEniCS`` class. It also
    inherits all attributes and methods from the
    ``SmoothstepScissionCompositeuFJCUFLFEniCS`` class, which inherits
    all attributes and methods from the ``CompositeuFJCUFLFEniCS``
    class.
    """
    def __init__(self, **kwargs):
        """
        Initializes the
        ``RateIndependentSmoothstepScissionCompositeuFJCUFLFEniCS``
        class, producing a composite uFJC single-chain model instance
        with rate-independent stochastic scission enforced via
        smoothstep scission implemented in the Unified Form Language
        (UFL) for FEniCS.
        
        Initialize and inherit all attributes and methods from the
        ``RateIndependentScissionUFLFEniCS`` class instance and the
        ``SmoothstepScissionCompositeuFJCUFLFEniCS`` class instance.
        """
        composite_ufjc = (
            RateIndependentSmoothstepScissionCompositeuFJC(**kwargs)
        )

        # Core composite uFJC single-chain model constants
        self.cond_val = Constant(composite_ufjc.cond_val)
        
        self.nu = Constant(composite_ufjc.nu)
        self.zeta_nu_char = Constant(composite_ufjc.zeta_nu_char)
        self.kappa_nu = Constant(composite_ufjc.kappa_nu)
        
        self.lmbda_nu_ref = Constant(composite_ufjc.lmbda_nu_ref)
        self.lmbda_c_eq_ref = Constant(composite_ufjc.lmbda_c_eq_ref)
        self.lmbda_nu_crit = Constant(composite_ufjc.lmbda_nu_crit)
        self.lmbda_c_eq_crit = Constant(composite_ufjc.lmbda_c_eq_crit)
        self.xi_c_crit = Constant(composite_ufjc.xi_c_crit)
        
        self.lmbda_c_eq_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_c_eq_pade2berg_crit)
        )
        self.lmbda_nu_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_nu_pade2berg_crit)
        )

        # Smoothstep scission model constants
        self.lmbda_nu_crit_min = Constant(composite_ufjc.lmbda_nu_crit_min)
        self.lmbda_nu_crit_max = Constant(composite_ufjc.lmbda_nu_crit_max)
        self.epsilon_nu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_nu_diss_hat_crit)
        )
        self.epsilon_cnu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_cnu_diss_hat_crit)
        )
        self.A_nu = Constant(composite_ufjc.A_nu)
        self.Lambda_nu_ref = Constant(composite_ufjc.Lambda_nu_ref)

        del composite_ufjc

        RateIndependentScissionUFLFEniCS.__init__(self)
        SmoothstepScissionCompositeuFJCUFLFEniCS.__init__(self)


class RateDependentSmoothstepScissionCompositeuFJCUFLFEniCS(
        RateDependentScissionUFLFEniCS,
        SmoothstepScissionCompositeuFJCUFLFEniCS):
    """The composite uFJC single-chain model class with rate-dependent
    stochastic scission enforced via smoothstep scission implemented in
    the Unified Form Language (UFL) for FEniCS.
    
    This class is a representation of the composite uFJC single-chain
    model with rate-dependent stochastic scission enforced via
    smoothstep scission implemented in the Unified Form Language (UFL)
    for FEniCS; an instance of this class is a composite uFJC
    single-chain model instance with rate-dependent stochastic scission
    enforced via smoothstep scission implemented in the Unified Form
    Language (UFL) for FEniCS. It also inherits all attributes and
    methods from the ``RateDependentScissionUFLFEniCS`` class. It also
    inherits all attributes and methods from the
    ``SmoothstepScissionCompositeuFJCUFLFEniCS`` class, which inherits
    all attributes and methods from the ``CompositeuFJCUFLFEniCS``
    class.
    """
    def __init__(self, **kwargs):
        """
        Initializes the
        ``RateDependentSmoothstepScissionCompositeuFJCUFLFEniCS`` class,
        producing a composite uFJC single-chain model instance with
        rate-dependent stochastic scission enforced via smoothstep 
        scission implemented in the Unified Form Language (UFL) for
        FEniCS.
        
        Initialize and inherit all attributes and methods from the
        ``RateDependentScissionUFLFEniCS`` class instance and the
        ``SmoothstepScissionCompositeuFJCUFLFEniCS`` class instance.
        """
        composite_ufjc = (
            RateDependentSmoothstepScissionCompositeuFJC(**kwargs)
        )

        # Core composite uFJC single-chain model constants
        self.cond_val = Constant(composite_ufjc.cond_val)
        
        self.nu = Constant(composite_ufjc.nu)
        self.zeta_nu_char = Constant(composite_ufjc.zeta_nu_char)
        self.kappa_nu = Constant(composite_ufjc.kappa_nu)
        
        self.lmbda_nu_ref = Constant(composite_ufjc.lmbda_nu_ref)
        self.lmbda_c_eq_ref = Constant(composite_ufjc.lmbda_c_eq_ref)
        self.lmbda_nu_crit = Constant(composite_ufjc.lmbda_nu_crit)
        self.lmbda_c_eq_crit = Constant(composite_ufjc.lmbda_c_eq_crit)
        self.xi_c_crit = Constant(composite_ufjc.xi_c_crit)
        
        self.lmbda_c_eq_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_c_eq_pade2berg_crit)
        )
        self.lmbda_nu_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_nu_pade2berg_crit)
        )

        # Smoothstep scission model constants
        self.lmbda_nu_crit_min = Constant(composite_ufjc.lmbda_nu_crit_min)
        self.lmbda_nu_crit_max = Constant(composite_ufjc.lmbda_nu_crit_max)
        self.epsilon_nu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_nu_diss_hat_crit)
        )
        self.epsilon_cnu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_cnu_diss_hat_crit)
        )
        self.A_nu = Constant(composite_ufjc.A_nu)
        self.Lambda_nu_ref = Constant(composite_ufjc.Lambda_nu_ref)

        # Rate dependent scission constant
        self.omega_0 = Constant(composite_ufjc.omega_0)

        del composite_ufjc

        RateDependentScissionUFLFEniCS.__init__(self)
        SmoothstepScissionCompositeuFJCUFLFEniCS.__init__(self)


class RateIndependentSigmoidScissionCompositeuFJCUFLFEniCS(
        RateIndependentScissionUFLFEniCS,
        SigmoidScissionCompositeuFJCUFLFEniCS):
    """The composite uFJC single-chain model class with rate-independent
    stochastic scission enforced via sigmoid scission implemented in the
    Unified Form Language (UFL) for FEniCS.
    
    This class is a representation of the composite uFJC single-chain
    model with rate-independent stochastic scission enforced via sigmoid
    scission implemented in the Unified Form Language (UFL) for FEniCS;
    an instance of this class is a composite uFJC single-chain model
    instance with rate-independent stochastic scission enforced via
    sigmoid scission implemented in the Unified Form Language (UFL) for
    FEniCS. It inherits all attributes and methods from the
    ``RateIndependentScissionUFLFEniCS`` class. It also inherits all
    attributes and methods from the
    ``SigmoidScissionCompositeuFJCUFLFEniCS`` class, which inherits all
    attributes and methods from the ``CompositeuFJCUFLFEniCS`` class.
    """
    def __init__(self, **kwargs):
        """
        Initializes the
        ``RateIndependentSigmoidScissionCompositeuFJCUFLFEniCS`` class,
        producing a composite uFJC single-chain model instance with
        rate-independent stochastic scission enforced via sigmoid
        scission implemented in the Unified Form Language (UFL) for
        FEniCS.
        
        Initialize and inherit all attributes and methods from the
        ``RateIndependentScissionUFLFEniCS`` class instance and the
        ``SigmoidScissionCompositeuFJCUFLFEniCS`` class instance.
        """
        composite_ufjc = (
            RateIndependentSigmoidScissionCompositeuFJC(**kwargs)
        )

        # Core composite uFJC single-chain model constants
        self.cond_val = Constant(composite_ufjc.cond_val)
        
        self.nu = Constant(composite_ufjc.nu)
        self.zeta_nu_char = Constant(composite_ufjc.zeta_nu_char)
        self.kappa_nu = Constant(composite_ufjc.kappa_nu)
        
        self.lmbda_nu_ref = Constant(composite_ufjc.lmbda_nu_ref)
        self.lmbda_c_eq_ref = Constant(composite_ufjc.lmbda_c_eq_ref)
        self.lmbda_nu_crit = Constant(composite_ufjc.lmbda_nu_crit)
        self.lmbda_c_eq_crit = Constant(composite_ufjc.lmbda_c_eq_crit)
        self.xi_c_crit = Constant(composite_ufjc.xi_c_crit)
        
        self.lmbda_c_eq_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_c_eq_pade2berg_crit)
        )
        self.lmbda_nu_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_nu_pade2berg_crit)
        )

        # Sigmoid scission model constants
        self.tau = Constant(composite_ufjc.tau)
        self.lmbda_nu_check = Constant(composite_ufjc.lmbda_nu_check)
        self.epsilon_nu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_nu_diss_hat_crit)
        )
        self.epsilon_cnu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_cnu_diss_hat_crit)
        )
        self.A_nu = Constant(composite_ufjc.A_nu)
        self.Lambda_nu_ref = Constant(composite_ufjc.Lambda_nu_ref)

        del composite_ufjc

        RateIndependentScissionUFLFEniCS.__init__(self)
        SigmoidScissionCompositeuFJCUFLFEniCS.__init__(self)


class RateDependentSigmoidScissionCompositeuFJCUFLFEniCS(
        RateDependentScissionUFLFEniCS,
        SigmoidScissionCompositeuFJCUFLFEniCS):
    """The composite uFJC single-chain model class with rate-dependent
    stochastic scission enforced via sigmoid scission implemented in the
    Unified Form Language (UFL) for FEniCS.
    
    This class is a representation of the composite uFJC single-chain
    model with rate-dependent stochastic scission enforced via sigmoid
    scission implemented in the Unified Form Language (UFL) for FEniCS;
    an instance of this class is a composite uFJC single-chain model
    instance with rate-dependent stochastic scission enforced via
    sigmoid scission implemented in the Unified Form Language (UFL) for
    FEniCS. It also inherits all attributes and methods from the
    ``RateDependentScissionUFLFEniCS`` class. It also inherits all
    attributes and methods from the
    ``SigmoidScissionCompositeuFJCUFLFEniCS`` class, which inherits all
    attributes and methods from the ``CompositeuFJCUFLFEniCS`` class.
    """
    def __init__(self, **kwargs):
        """
        Initializes the
        ``RateDependentSigmoidScissionCompositeuFJCUFLFEniCS`` class,
        producing a composite uFJC single-chain model instance with
        rate-dependent stochastic scission enforced via sigmoid 
        scission.
        
        Initialize and inherit all attributes and methods from the
        ``RateDependentScissionUFLFEniCS`` class instance and the
        ``SigmoidScissionCompositeuFJCUFLFEniCS`` class instance.
        """
        composite_ufjc = (
            RateDependentSigmoidScissionCompositeuFJC(**kwargs)
        )

        # Core composite uFJC single-chain model constants
        self.cond_val = Constant(composite_ufjc.cond_val)
        
        self.nu = Constant(composite_ufjc.nu)
        self.zeta_nu_char = Constant(composite_ufjc.zeta_nu_char)
        self.kappa_nu = Constant(composite_ufjc.kappa_nu)
        
        self.lmbda_nu_ref = Constant(composite_ufjc.lmbda_nu_ref)
        self.lmbda_c_eq_ref = Constant(composite_ufjc.lmbda_c_eq_ref)
        self.lmbda_nu_crit = Constant(composite_ufjc.lmbda_nu_crit)
        self.lmbda_c_eq_crit = Constant(composite_ufjc.lmbda_c_eq_crit)
        self.xi_c_crit = Constant(composite_ufjc.xi_c_crit)
        
        self.lmbda_c_eq_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_c_eq_pade2berg_crit)
        )
        self.lmbda_nu_pade2berg_crit = (
            Constant(composite_ufjc.lmbda_nu_pade2berg_crit)
        )

        # Sigmoid scission model constants
        self.tau = Constant(composite_ufjc.tau)
        self.lmbda_nu_check = Constant(composite_ufjc.lmbda_nu_check)
        self.epsilon_nu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_nu_diss_hat_crit)
        )
        self.epsilon_cnu_diss_hat_crit = (
            Constant(composite_ufjc.epsilon_cnu_diss_hat_crit)
        )
        self.A_nu = Constant(composite_ufjc.A_nu)
        self.Lambda_nu_ref = Constant(composite_ufjc.Lambda_nu_ref)

        # Rate dependent scission constant
        self.omega_0 = Constant(composite_ufjc.omega_0)

        del composite_ufjc

        RateDependentScissionUFLFEniCS.__init__(self)
        SigmoidScissionCompositeuFJCUFLFEniCS.__init__(self)