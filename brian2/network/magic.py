from ..units import check_units, second
from ..base import BrianObject, get_instances
from .network import Network
import network

__all__ = ['MagicNetwork',
           'run', 'reinit', 'stop',
           ]


class MagicNetwork(Network):
    '''
    Network that automatically adds all Brian objects
    
    See Also
    --------
    
    Network, run, reinit, stop
    '''
    def __init__(self):
        super(MagicNetwork, self).__init__()
        self.add(get_instances(BrianObject))


@check_units(duration=second, report_period=second)
def run(duration, report=None, report_period=60*second):
    '''
    Runs a simulation with all Brian objects for the given duration.
    
    Parameters
    ----------
    
    duration : Quantity
        The amount of simulation time to run for.
    report : {None, 'stdout', 'stderr', 'graphical', function}, optional
        How to report the progress of the simulation. If None, do not
        report progress. If stdout or stderr is specified, print the
        progress to stdout or stderr. If graphical, Tkinter is used to
        show a graphical progress bar. Alternatively, you can specify
        a callback ``function(elapsed, complete)`` which will be passed
        the amount of time elapsed (in seconds) and the fraction complete
        from 0 to 1.
    report_period : Quantity
        How frequently (in real time) to report progress.
        
    Notes
    -----
    
    The simulation Network will include all defined Brian objects.
    
    The simulation can be stopped by calling the global :func:`stop` function.
    
    See Also
    --------
    
    MagicNetwork, reinit, stop
    '''
    net = MagicNetwork()
    net.run(duration, report=report, report_period=report_period)

def reinit():
    '''
    Reinitialises all Brian objects.
    
    See Also
    --------
    
    MagicNetwork, run, stop
    '''
    net = MagicNetwork()
    net.reinit()

def stop():
    '''
    Stops all running simulations.
    
    See Also
    --------
    
    MagicNetwork, run, reinit
    '''
    network.globally_stopped = True

# TODO: clear (still needed? maybe?)
# TODO: forget (rename?)
# TODO: recall (rename?)
